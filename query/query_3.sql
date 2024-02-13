SELECT groups.name AS group_name, subjects.name AS subject, ROUND(AVG(grades.grade), 2) AS average_grade
FROM groups
JOIN students ON groups.id = students.group_id_fn
JOIN grades ON students.id = grades.student_id_fn
JOIN subjects ON grades.subject_id_fn = subjects.id
WHERE subjects.id = 4
GROUP BY groups.name
ORDER BY average_grade DESC;
