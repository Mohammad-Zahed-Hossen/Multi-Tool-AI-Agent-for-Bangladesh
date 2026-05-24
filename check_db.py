import sqlite3
import pandas as pd


def inspect_database(db_path, table_name):

    print(f"\nInspecting: {db_path}")

    conn = sqlite3.connect(db_path)

    # Show table schema
    schema_query = f"PRAGMA table_info({table_name});"

    schema = pd.read_sql_query(schema_query, conn)

    print("\nSchema:")
    print(schema)

    # Show sample rows
    sample_query = f"SELECT * FROM {table_name} LIMIT 5"

    sample = pd.read_sql_query(sample_query, conn)

    print("\nSample Rows:")
    print(sample)

    conn.close()


inspect_database(
    "databases/institutions.db",
    "institutions"
)

inspect_database(
    "databases/hospitals.db",
    "hospitals"
)

inspect_database(
    "databases/restaurants.db",
    "restaurants"
)
