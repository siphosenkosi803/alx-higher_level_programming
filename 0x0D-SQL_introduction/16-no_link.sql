-- List all records in MYSQL server
-- Select all records with the name in descending order of hbtn_0c_0
SELECT 'score', 'name'
FROM 'second_table'
WHERE 'name' IS NOT NULL
ORDER BY 'score' DESC;
