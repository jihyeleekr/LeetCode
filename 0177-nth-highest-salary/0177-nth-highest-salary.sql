CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT
BEGIN
  RETURN (
    # Write your MySQL query statement below.
    SELECT DISTINCT(salary)
    FROM
		(SELECT salary, dense_rank () OVER( ORDER BY salary DESC ) AS r 
        FROM Employee) AS ranked
	WHERE r = N
  );
END