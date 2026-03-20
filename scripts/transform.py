import pandas as pd
import os

RAW_PATH = "data/raw"
PROCESSED_PATH = "data/processed"


def load_data():
    data = {}
    for file in os.listdir(RAW_PATH):
        if file.endswith(".csv"):
            path = os.path.join(RAW_PATH, file)
            data[file] = pd.read_csv(path)
    return data


def save_data(df, name):
    os.makedirs(PROCESSED_PATH, exist_ok=True)
    df.to_csv(os.path.join(PROCESSED_PATH, name), index=False)


def transform():
    data = load_data()

    # Extract tables
    orders = data["olist_orders_dataset.csv"]
    customers = data["olist_customers_dataset.csv"]
    items = data["olist_order_items_dataset.csv"]
    payments = data["olist_order_payments_dataset.csv"]
    products = data["olist_products_dataset.csv"]

    # --- CLEANING STARTS HERE ---

    # 1. Convert date columns
    date_cols = [
        "order_purchase_timestamp",
        "order_approved_at",
        "order_delivered_carrier_date",
        "order_delivered_customer_date",
        "order_estimated_delivery_date"
    ]

    for col in date_cols:
        orders[col] = pd.to_datetime(orders[col], errors='coerce')

    # 2. Remove duplicates
    orders = orders.drop_duplicates()
    customers = customers.drop_duplicates()
    items = items.drop_duplicates()
    payments = payments.drop_duplicates()
    products = products.drop_duplicates()

    # 3. Handle missing values
    orders = orders.dropna(subset=["order_purchase_timestamp"])

    # --- FEATURE ENGINEERING ---

    # Delivery time
    orders["delivery_time_days"] = (
        orders["order_delivered_customer_date"] - orders["order_purchase_timestamp"]
    ).dt.days
    orders = orders[orders["delivery_time_days"] >= 0]

    # Order month
    orders["order_month"] = orders["order_purchase_timestamp"].dt.to_period("M").astype(str)

    # Total order value (aggregate payments)
    order_value = payments.groupby("order_id")["payment_value"].sum().reset_index()
    order_value.rename(columns={"payment_value": "total_order_value"}, inplace=True)

    orders = orders.merge(order_value, on="order_id", how="left")

    # --- SAVE CLEAN DATA ---

    save_data(orders, "orders_clean.csv")
    save_data(customers, "customers_clean.csv")
    save_data(items, "items_clean.csv")
    save_data(payments, "payments_clean.csv")
    save_data(products, "products_clean.csv")

    print("Transformation completed successfully.")


if __name__ == "__main__":
    transform()