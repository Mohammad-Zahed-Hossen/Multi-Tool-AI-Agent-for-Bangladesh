import pandas as pd
import sqlite3
import os

os.makedirs("databases", exist_ok=True)

def clean_column_names(df):
    """
    Clean dataframe column names.
    """

    df.columns = (
        df.columns
        .str.strip()
        .str.lower()
        .str.replace(" ", "_")
        .str.replace("-", "_")
        .str.replace(r"[^\w\s]", "", regex=True)
    )

    return df


def csv_to_sqlite(csv_path, db_path, table_name):
    print(f"\nProcessing: {csv_path}")

    df = pd.read_csv(csv_path)

    print("\nOriginal Columns:")
    print(df.columns.tolist())

    df = clean_column_names(df)

    print("\nCleaned Columns:")
    print(df.columns.tolist())

    df = df.drop_duplicates()
    df = df.fillna("Unknown")

    conn = sqlite3.connect(db_path)

    df.to_sql(
        table_name,
        conn,
        if_exists="replace",
        index=False
    )

    cursor = conn.cursor()
    cursor.execute(f"SELECT COUNT(*) FROM {table_name}")
    total_rows = cursor.fetchone()[0]

    print(f"\nInserted Rows: {total_rows}")

    sample_query = f"SELECT * FROM {table_name} LIMIT 3"
    sample_df = pd.read_sql_query(sample_query, conn)

    print("\nSample Data:")
    print(sample_df)

    conn.close()
    print(f"\nDatabase Created: {db_path}")


csv_to_sqlite(
    csv_path="data/institutions.csv",
    db_path="databases/institutions.db",
    table_name="institutions"
)

csv_to_sqlite(
    csv_path="data/hospitals.csv",
    db_path="databases/hospitals.db",
    table_name="hospitals"
)

csv_to_sqlite(
    csv_path="data/restaurants.csv",
    db_path="databases/restaurants.db",
    table_name="restaurants"
)

print("\nAll databases created successfully.")
