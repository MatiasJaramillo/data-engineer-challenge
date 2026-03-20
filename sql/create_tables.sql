DROP TABLE IF EXISTS fact_orders;
DROP TABLE IF EXISTS dim_customers;
DROP TABLE IF EXISTS dim_products;
DROP TABLE IF EXISTS fact_order_items;
DROP TABLE IF EXISTS fact_payments;
DROP TABLE IF EXISTS fact_reviews;
DROP TABLE IF EXISTS dim_sellers;

CREATE TABLE dim_customers (
    customer_id TEXT PRIMARY KEY,
    customer_unique_id TEXT,
    customer_zip_code_prefix INTEGER,
    customer_city TEXT,
    customer_state TEXT
);

CREATE TABLE dim_products (
    product_id TEXT PRIMARY KEY,
    product_category_name TEXT,
    product_name_lenght REAL,
    product_description_lenght REAL,
    product_photos_qty REAL,
    product_weight_g REAL,
    product_length_cm REAL,
    product_height_cm REAL,
    product_width_cm REAL
);

CREATE TABLE dim_sellers (
    seller_id TEXT PRIMARY KEY,
    seller_zip_code_prefix INTEGER,
    seller_city TEXT,
    seller_state TEXT
);

CREATE TABLE fact_orders (
    order_id TEXT PRIMARY KEY,
    customer_id TEXT,
    order_status TEXT,
    order_purchase_timestamp TEXT,
    order_approved_at TEXT,
    order_delivered_carrier_date TEXT,
    order_delivered_customer_date TEXT,
    order_estimated_delivery_date TEXT,
    delivery_time_days REAL,
    order_month TEXT,
    total_order_value REAL,
    FOREIGN KEY (customer_id) REFERENCES dim_customers(customer_id)
);

CREATE TABLE fact_order_items (
    order_id TEXT,
    order_item_id INTEGER,
    product_id TEXT,
    seller_id TEXT,
    shipping_limit_date TEXT,
    price REAL,
    freight_value REAL,
    PRIMARY KEY (order_id, order_item_id),
    FOREIGN KEY (order_id) REFERENCES fact_orders(order_id),
    FOREIGN KEY (product_id) REFERENCES dim_products(product_id),
    FOREIGN KEY (seller_id) REFERENCES dim_sellers(seller_id)
);

CREATE TABLE fact_payments (
    order_id TEXT,
    payment_sequential INTEGER,
    payment_type TEXT,
    payment_installments INTEGER,
    payment_value REAL,
    PRIMARY KEY (order_id, payment_sequential),
    FOREIGN KEY (order_id) REFERENCES fact_orders(order_id)
);

CREATE TABLE fact_reviews (
    review_id TEXT,
    order_id TEXT,
    review_score REAL,
    review_comment_title TEXT,
    review_comment_message TEXT,
    review_creation_date TEXT,
    review_answer_timestamp TEXT,
    PRIMARY KEY (review_id, order_id),
    FOREIGN KEY (order_id) REFERENCES fact_orders(order_id)
);