-- Write your PostgreSQL query statement below
SELECT product_id 
FROM products p
WHERE low_fats = 'Y' and recyclable = 'Y'