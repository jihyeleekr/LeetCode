# Write your MySQL query statement below
WITH cte AS (

(SELECT p.user_id, p.product_id, pi.category
FROM ProductPurchases p
LEFT JOIN ProductInfo pi
ON p.product_id = pi.product_id)

)

SELECT p1.product_id AS product1_id, p2.product_id AS product2_id, p1.category AS product1_category, p2.category AS product2_category, COUNT(p1.user_id) AS customer_count
FROM cte p1
LEFT JOIN cte p2
ON p1.product_id != p2.product_id AND p1.user_id = p2.user_id
WHERE p1.product_id < p2.product_id
GROUP BY product1_id , product2_id
HAVING COUNT(p1.user_id) >=3
ORDER BY customer_count DESC, product1_id ASC, product2_id ASC


