# Write your MySQL query statement below
SELECT product_id, year AS first_year, quantity, price
FROM
(SELECT *, DENSE_RANK() OVER (
    PARTITION BY product_id
    ORDER BY year ASC
) AS r
FROM Sales) AS ranked
WHERE r = 1
GROUP BY product_id, price

