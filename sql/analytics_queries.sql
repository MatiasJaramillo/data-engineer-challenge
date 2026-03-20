-- Q1: Monthly transaction volume
SELECT
    order_month,
    COUNT(*) AS total_orders
FROM fact_orders
GROUP BY order_month
ORDER BY order_month;

-- Q2: Top 10 product categories by generated value
SELECT
    dp.product_category_name,
    ROUND(SUM(foi.price + foi.freight_value), 2) AS total_value
FROM fact_order_items foi
JOIN dim_products dp
    ON foi.product_id = dp.product_id
GROUP BY dp.product_category_name
ORDER BY total_value DESC
LIMIT 10;

-- Q3: Average time between purchase and delivery
SELECT
    ROUND(AVG(delivery_time_days), 2) AS avg_delivery_time_days
FROM fact_orders
WHERE delivery_time_days IS NOT NULL;

-- Q4: Percentage of negative outcomes (review score <= 2 OR canceled orders)
WITH total_orders AS (
    SELECT COUNT(DISTINCT order_id) AS total FROM fact_orders
),
negative_orders AS (
    SELECT COUNT(DISTINCT fo.order_id) AS negative_count
    FROM fact_orders fo
    LEFT JOIN fact_reviews fr
        ON fo.order_id = fr.order_id
    WHERE fo.order_status = 'canceled'
       OR fr.review_score <= 2
)
SELECT
    ROUND(100.0 * negative_count / total, 2) AS negative_outcome_percentage
FROM total_orders, negative_orders;

-- Q5: Custom business question
-- Do delayed deliveries correlate with worse review scores?
SELECT
    CASE
        WHEN fo.delivery_time_days > 10 THEN 'Delayed'
        ELSE 'On Time / Faster'
    END AS delivery_group,
    ROUND(AVG(fr.review_score), 2) AS avg_review_score,
    COUNT(*) AS total_reviews
FROM fact_orders fo
JOIN fact_reviews fr
    ON fo.order_id = fr.order_id
WHERE fo.delivery_time_days IS NOT NULL
  AND fr.review_score IS NOT NULL
GROUP BY delivery_group;