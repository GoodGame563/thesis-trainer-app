from os import makedirs, path

from .db_connection import db_connect
from .structure import AllGames, Players, Roles, Teams, Transfers

data_path = "data"


async def create_db():
    if not path.exists(data_path):
        makedirs("data")
    await init_database()


async def _create_table(cur, schema_cls):
    columns = schema_cls.get_columns()
    col_defs = ",\n    ".join(f"{name} {typ}" for name, typ in columns)
    fkey_defs = (
        ",\n    ".join(schema_cls.__foreign_keys__)
        if schema_cls.__foreign_keys__
        else ""
    )
    separator = ",\n    " if fkey_defs else ""
    sql = f"CREATE TABLE {schema_cls.__tablename__} (\n    {col_defs}{separator}{fkey_defs}\n)"
    await cur.execute(sql)


async def _recreate_table(cur, schema_cls):
    old_name = schema_cls.__tablename__
    new_name = f"{old_name}_new"

    await cur.execute("PRAGMA foreign_keys")
    fk_was_on = await cur.fetchone()[0] == 1
    if fk_was_on:
        await cur.execute("PRAGMA foreign_keys = OFF")

    try:
        columns = schema_cls.get_columns()
        col_defs = ",\n    ".join(f"{name} {typ}" for name, typ in columns)
        fkey_defs = (
            ",\n    ".join(schema_cls.__foreign_keys__)
            if schema_cls.__foreign_keys__
            else ""
        )
        separator = ",\n    " if fkey_defs else ""
        await cur.execute(
            f"CREATE TABLE {new_name} (\n    {col_defs}{separator}{fkey_defs}\n)"
        )

        await cur.execute(f"PRAGMA table_info({old_name})")
        old_cols = [row[1] for row in cur.fetchall()]
        await cur.execute(f"PRAGMA table_info({new_name})")
        new_cols = [row[1] for row in cur.fetchall()]
        common = [c for c in old_cols if c in new_cols]

        if common:
            cols = ", ".join(common)
            await cur.execute(
                f"INSERT INTO {new_name} ({cols}) SELECT {cols} FROM {old_name}"
            )

        await cur.execute(f"DROP TABLE {old_name}")
        await cur.execute(f"ALTER TABLE {new_name} RENAME TO {old_name}")
    finally:
        if fk_was_on:
            await cur.execute("PRAGMA foreign_keys = ON")


async def init_database():
    schemas = [Players, Teams, Roles, AllGames, Transfers]
    conn = await db_connect()
    await conn.execute("PRAGMA foreign_keys = ON")
    cur = await conn.cursor()

    for schema_cls in schemas:
        await cur.execute(
            "SELECT name FROM sqlite_master WHERE type='table' AND name=?",
            (schema_cls.__tablename__,),
        )
        exists = await cur.fetchone() is not None

        if exists:
            await cur.execute(f"PRAGMA table_info({schema_cls.__tablename__})")
            existing = [(row[1].lower(), row[2].upper()) for row in await cur.fetchall()]
            expected = [
                (name.lower(), typ.split()[0].upper())
                for name, typ in schema_cls.get_columns()
            ]
            if existing != expected:
                await _recreate_table(cur, schema_cls)
        else:
            await _create_table(cur, schema_cls)

    await conn.commit()
    await conn.close()
