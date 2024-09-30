SELECT sub.subject_name
FROM grades g
JOIN subjects sub ON g.subject_id = sub.id
JOIN students s ON g.student_id = s.id
WHERE s.id = 2
