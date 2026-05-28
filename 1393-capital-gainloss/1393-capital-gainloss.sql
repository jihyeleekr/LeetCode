# Write your MySQL query statement below
SELECT buy.stock_name,  (total_sell - total_buy) AS capital_gain_loss
FROM
(SELECT stock_name, SUM(price) AS total_buy
FROM Stocks 
WHERE operation = 'Buy'
GROUP BY stock_name) AS buy
LEFT JOIN
(SELECT stock_name, SUM(price) AS total_sell
FROM Stocks
WHERE operation = 'Sell'
GROUP BY stock_name) AS sell
ON buy.stock_name = sell.stock_name