import os
import sqlite3
import pandas as pd

DB_PATH = "db/olist.db"
PROCESSED_PATH = "data/processed"
SQL_SCHEMA_PATH = "sql/create_tables.sql"


def load_csv(name):
    path = os.path.join(PROCESSED_PATH, name)
    return pd.read_csv(path)


def create_database():
    conn = sqlite3.connect(DB_PATH)
    with open(SQL_SCHEMA_PATH, "r", encoding="utf-8") as f:
        conn.executescript(f.read())
    conn.commit()
    return conn


def load_tables(conn):
    customers = load_csv("customers_clean.csv")
    products = load_csv("products_clean.csv")
    sellers = load_csv("sellers_clean.csv")
    orders = load_csv("orders_clean.csv")
    items = load_csv("items_clean.csv")
    payments = load_csv("payments_clean.csv")
    reviews = load_csv("reviews_clean.csv")

    customers.to_sql("dim_customers", conn, if_exists="append", index=False)
    products.to_sql("dim_products", conn, if_exists="append", index=False)
    sellers.to_sql("dim_sellers", conn, if_exists="append", index=False)
    orders.to_sql("fact_orders", conn, if_exists="append", index=False)
    items.to_sql("fact_order_items", conn, if_exists="append", index=False)
    payments.to_sql("fact_payments", conn, if_exists="append", index=False)
    reviews.to_sql("fact_reviews", conn, if_exists="append", index=False)

    print("All tables loaded successfully.")


def validate_load(conn):
    tables = [
        "dim_customers",
        "dim_products",
        "dim_sellers",
        "fact_orders",
        "fact_order_items",
        "fact_payments",
        "fact_reviews"
    ]

    for table in tables:
        count = pd.read_sql_query(f"SELECT COUNT(*) AS count FROM {table}", conn)
        print(f"{table}: {count.loc[0, 'count']} rows")


if __name__ == "__main__":
    os.makedirs("db", exist_ok=True)
    conn = create_database()
    load_tables(conn)
    validate_load(conn)
    conn.close()