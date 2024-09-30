SELECT s.student_name, AVG(g.grade) AS average_grade
FROM students s
JOIN grades g ON s.id = g.student_id
WHERE g.subject_id = SUBJECT_ID
GROUP BY s.id
ORDER BY average_grade DESC
LIMIT 1;
