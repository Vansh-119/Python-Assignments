CREATE DATABASE data_bank;
USE data_bank;

CREATE TABLE regions (
    region_id INT,
    region_name VARCHAR(20)
);

CREATE TABLE customer_nodes (
    customer_id INT,
    region_id INT,
    node_id INT,
    start_date DATE,
    end_date DATE
);

CREATE TABLE customer_transactions (
    customer_id INT,
    txn_date DATE,
    txn_type VARCHAR(20),
    txn_amount INT
);


--1
SELECT COUNT(DISTINCT node_id) as unique_nodes FROM customer_nodes;

--2
SELECT r.region_name,count(DISTINCT c.node_id) as nodesPerRegion
from customer_nodes c JOIN regions r 
ON c.region_id=r.region_id group by r.region_name
order by r.region_name;

--3
SELECT r.region_name,count(DISTINCT c.customer_id) as customers 
from regions r JOIN customer_nodes c ON r.region_id=c.region_id
group by r.region_name;

--4
SELECT AVG(end_date - start_date) AS avg_days 
from customer_nodes where end_date <>'9999-12-31';

--5
WITH reallocation_days AS (
    SELECT
        r.region_name,
        (c.end_date - c.start_date) AS days_reallocated
    FROM customer_nodes c
    JOIN regions r
        ON c.region_id = r.region_id
    WHERE c.end_date <> '9999-12-31'
)

SELECT DISTINCT
    region_name,
    PERCENTILE_CONT(0.50) WITHIN GROUP (ORDER BY days_reallocated)
        OVER (PARTITION BY region_name) AS median,
    PERCENTILE_CONT(0.80) WITHIN GROUP (ORDER BY days_reallocated)
        OVER (PARTITION BY region_name) AS percentile_80,
    PERCENTILE_CONT(0.95) WITHIN GROUP (ORDER BY days_reallocated)
        OVER (PARTITION BY region_name) AS percentile_95
FROM reallocation_days
ORDER BY region_name;

--6
SELECT txn_type,COUNT(*),sum(txn_amount) from customer_transactions group by txn_type;

--7
WITH customer_deposits AS (
    SELECT
        customer_id,
        COUNT(*) AS deposit_count,
        SUM(txn_amount) AS total_deposit_amount
    FROM customer_transactions
    WHERE txn_type = 'deposit'
    GROUP BY customer_id
)

SELECT
    ROUND(AVG(deposit_count), 2) AS avg_deposit_count,
    ROUND(AVG(total_deposit_amount), 2) AS avg_deposit_amount
FROM customer_deposits;


--8
WITH monthly_transactions AS (
    SELECT
        customer_id,
        MONTH(txn_date) AS month_num,
        SUM(CASE WHEN txn_type = 'deposit' THEN 1 ELSE 0 END) AS deposit_count,
        SUM(CASE WHEN txn_type = 'purchase' THEN 1 ELSE 0 END) AS purchase_count,
        SUM(CASE WHEN txn_type = 'withdrawal' THEN 1 ELSE 0 END) AS withdrawal_count
    FROM customer_transactions
    GROUP BY customer_id, MONTH(txn_date)
)

SELECT
    month_num,
    COUNT(*) AS customer_count
FROM monthly_transactions
WHERE deposit_count > 1
  AND (purchase_count >= 1 OR withdrawal_count >= 1)
GROUP BY month_num
ORDER BY month_num;