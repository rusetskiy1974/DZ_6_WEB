SELECT s.fullname AS name, subjects.name AS subject_name, t.fullname AS teacher_name, g.grade_date AS data
FROM students s
JOIN grades g ON s.id = g.student_id_fn
JOIN subjects ON g.subject_id_fn = subjects.id
JOIN teachers t ON subjects.teacher_id_fn  = t.id
WHERE s.id = 20 AND t.id = 3
ORDER BY data;
