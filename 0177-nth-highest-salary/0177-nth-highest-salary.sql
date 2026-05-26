CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT
BEGIN
  RETURN (
      # Write your MySQL query statement below.
        SELECT salary
        FROM (SELECT DISTINCT salary, 
            dense_rank () OVER(
            ORDER BY salary DESC) AS r 
            FROM Employee
        ) AS ranked
        WHERE r = N
        LIMIT 1
  );
END