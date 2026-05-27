# Write your MySQL query statement below
SELECT MAX(num) AS num
FROM (SELECT num, COUNT(*) AS total
FROM Mynumbers
GROUP BY num) AS grouped
WHERE total = 1
