SELECT s.fullname AS student_name, subjects.name as subject, ROUND(AVG(grades.grade), 2) AS average_grade
FROM students s
JOIN grades ON s.id = grades.student_id_fn
JOIN subjects ON grades.subject_id_fn = subjects.id
WHERE subjects.id = 4
GROUP BY s.id
ORDER BY average_grade DESC
LIMIT 1;
