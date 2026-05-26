# Write your MySQL query statement below

/* Check list
1. combine two table ✔
2. check whether both client_id and driver_id are not banned
3. group by 'reqeust_at'
4. calculate cancellation rate = # of cancelled / # total requests
*/

SELECT request_at AS Day, ROUND(SUM(status LIKE 'cancelled%') / COUNT(status), 2) AS 'Cancellation Rate'
FROM (SELECT *
FROM Trips t
JOIN Users u
ON (u.role = 'client' AND u.users_id = t.client_id) OR (u.role = 'driver' AND u.users_id = t.driver_id)
WHERE banned = 'No' AND (request_at BETWEEN '2013-10-01' AND '2013-10-03')
GROUP BY t.id
HAVING COUNT(*) = 2
) AS bind
GROUP BY request_at 


