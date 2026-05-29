# Write your MySQL query statement below
SELECT p2.user_id, prompt_count, avg_tokens
FROM prompts p
LEFT JOIN 
(SELECT user_id, COUNT(*) AS prompt_count, ROUND(AVG(tokens),2) AS avg_tokens
FROM prompts
GROUP BY user_id
HAVING COUNT(*) >= 3) AS p2
ON p.user_id = p2.user_id
GROUP BY user_id
HAVING MAX(tokens) > avg_tokens
ORDER BY avg_tokens DESC, user_id ASC
