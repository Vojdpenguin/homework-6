SELECT AVG(g.grade) AS average_grade
FROM grades g
JOIN students s ON g.student_id = s.id
JOIN subjects sub ON g.subject_id = sub.id
JOIN teachers t ON sub.teacher_id = t.id
WHERE s.id = 1
AND t.id = 1

