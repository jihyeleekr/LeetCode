# Write your MySQL query statement below
SELECT DISTINCT p.email AS Email
FROM Person AS p 
JOIN Person AS d
WHERE p.id <> d.id AND p.email = d.email