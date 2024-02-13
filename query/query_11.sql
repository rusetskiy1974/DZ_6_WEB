SELECT s.fullname AS name, ROUND(AVG(g.grade),2 ) AS average_grade, t.fullname AS teacher_name
FROM students s
JOIN grades g ON s.id = g.student_id_fn
JOIN subjects ON g.subject_id_fn = subjects.id
JOIN teachers t ON subjects.teacher_id_fn = t.id
WHERE s.id = 8 AND t.id = 3;
