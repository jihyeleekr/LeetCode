# Write your MySQL query statement below
/*SELECT customer_id
FROM 
(SELECT DISTINCT customer_id, (COUNT(product_key)) AS total_order
FROM Customer
GROUP BY customer_id) total
WHERE total.total_order = 
(SELECT COUNT(*)
FROM Product)*/

SELECT customer_id
FROM (SELECT DISTINCT *, DENSE_RANK() OVER(
    PARTITION BY customer_id
    ORDER BY product_key 
) AS total_order
FROM Customer) AS total
GROUP BY customer_id 
HAVING COUNT(total_order) = (SELECT COUNT(*) FROM Product)

