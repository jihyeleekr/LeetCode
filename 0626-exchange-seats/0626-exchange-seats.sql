# Write your MySQL query statement below
SELECT s.id,
CASE 
    WHEN s.id = sorted.odd_id AND even_student IS NOT NULL THEN even_student
    WHEN s.id = sorted.even_id THEN odd_student
    ELSE odd_student
END AS student
FROM Seat s
JOIN (SELECT 
    s1.id AS odd_id,
    s1.student AS odd_student,
    s2.id AS even_id,
    s2.student AS even_student
FROM Seat s1
LEFT JOIN Seat s2 ON s1.id = s2.id - 1
WHERE s1.id % 2 = 1) AS sorted
ON s.id = even_id OR s.id = odd_id
ORDER BY s.id ASC


