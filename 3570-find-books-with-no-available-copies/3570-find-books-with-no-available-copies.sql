# Write your MySQL query statement below
/*
Check list:
    1.combine two table 
    2. Count # of NULL in return_date for each book
    3. IF SUM of NULL for each book = # of copies then select
*/

SELECT l.book_id, title, author, genre, publication_year, total_copies AS current_borrowers
FROM library_books l
JOIN borrowing_records b
USING (book_id)
WHERE b.return_date IS NULL
GROUP BY l.book_id
HAVING COUNT(*) = total_copies
ORDER BY current_borrowers DESC, title






