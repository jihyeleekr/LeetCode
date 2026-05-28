# Write your MySQL query statement below
WITH cte AS (
(SELECT buyer_id, COUNT(order_date) AS orders_in_2019
FROM Orders
WHERE order_date LIKE '2019-%'
GROUP BY buyer_id
) 
)

SELECT user_id AS buyer_id, join_date, 
CASE
    WHEN orders_in_2019 IS NULL THEN 0
    ELSE orders_in_2019
END AS
orders_in_2019
FROM Users u
LEFT JOIN cte
ON u.user_id = buyer_id


