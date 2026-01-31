from os import makedirs, path


from .structure import Players, Teams, Roles, AllGames, Transfers
from .db_connection import db_connect

data_path = "data"


def create_db():
    if not path.exists(data_path):
        makedirs("data")
    init_database()


def _create_table(cur, schema_cls):
    columns = schema_cls.get_columns()
    col_defs = ",\n    ".join(f"{name} {typ}" for name, typ in columns)
    fkey_defs = (
        ",\n    ".join(schema_cls.__foreign_keys__)
        if schema_cls.__foreign_keys__
        else ""
    )
    separator = ",\n    " if fkey_defs else ""
    sql = f"CREATE TABLE {schema_cls.__tablename__} (\n    {col_defs}{separator}{fkey_defs}\n)"
    cur.execute(sql)


def _recreate_table(cur, schema_cls):
    old_name = schema_cls.__tablename__
    new_name = f"{old_name}_new"

    cur.execute("PRAGMA foreign_keys")
    fk_was_on = cur.fetchone()[0] == 1
    if fk_was_on:
        cur.execute("PRAGMA foreign_keys = OFF")

    try:
        columns = schema_cls.get_columns()
        col_defs = ",\n    ".join(f"{name} {typ}" for name, typ in columns)
        fkey_defs = ",\n    ".join(schema_cls.__foreign_keys__) if schema_cls.__foreign_keys__ else ""
        separator = ",\n    " if fkey_defs else ""
        cur.execute(f"CREATE TABLE {new_name} (\n    {col_defs}{separator}{fkey_defs}\n)")

        cur.execute(f"PRAGMA table_info({old_name})")
        old_cols = [row[1] for row in cur.fetchall()]
        cur.execute(f"PRAGMA table_info({new_name})")
        new_cols = [row[1] for row in cur.fetchall()]
        common = [c for c in old_cols if c in new_cols]

        if common:
            cols = ", ".join(common)
            cur.execute(f"INSERT INTO {new_name} ({cols}) SELECT {cols} FROM {old_name}")

        cur.execute(f"DROP TABLE {old_name}")
        cur.execute(f"ALTER TABLE {new_name} RENAME TO {old_name}")
    finally:
        if fk_was_on:
            cur.execute("PRAGMA foreign_keys = ON")


def init_database():
    schemas = [Players, Teams, Roles, AllGames, Transfers]
    conn = db_connect()
    conn.execute("PRAGMA foreign_keys = ON")
    cur = conn.cursor()

    for schema_cls in schemas:
        cur.execute(
            "SELECT name FROM sqlite_master WHERE type='table' AND name=?",
            (schema_cls.__tablename__,),
        )
        exists = cur.fetchone() is not None

        if exists:
            cur.execute(f"PRAGMA table_info({schema_cls.__tablename__})")
            existing = [(row[1].lower(), row[2].upper()) for row in cur.fetchall()]
            expected = [
                (name.lower(), typ.split()[0].upper())
                for name, typ in schema_cls.get_columns()
            ]
            if existing != expected:
                _recreate_table(cur, schema_cls)
        else:
            _create_table(cur, schema_cls)

    conn.commit()
    conn.close()

