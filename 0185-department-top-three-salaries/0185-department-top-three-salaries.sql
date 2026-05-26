# Write your MySQL query statement below
SELECT Department, Employee, Salary
FROM
(SELECT Department, Employee, Salary, DENSE_RANK() OVER(
    PARTITION BY Department
    ORDER BY Salary DESC
) AS r
FROM
    (SELECT d.name AS Department, e.name AS Employee, e.salary AS Salary
    FROM Employee e LEFT JOIN Department d ON e.departmentId = d.id
    ) AS sorted)
AS  ranked
WHERE r <= 3

