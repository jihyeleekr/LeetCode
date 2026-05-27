# Write your MySQL query statement below
with added_up as (
    (
        SELECT requester_id AS id, COUNT(accepter_id) as partial_count
        FROM RequestAccepted
        GROUP BY requester_id
    )
    union all
    (
        SELECT accepter_id AS id, COUNT(requester_id) as partial_count
        FROM RequestAccepted
        GROUP BY accepter_id
    )
)

SELECT id, SUM(partial_count) AS num
FROM added_up
GROUP BY id
ORDER BY num DESC
LIMIT 1


