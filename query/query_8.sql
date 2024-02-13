SELECT teachers.fullname AS teacher_name, subjects.name AS subject_name, ROUND(AVG(grades.grade), 2) AS average_grade
FROM teachers
JOIN subjects ON teachers.id = subjects.teacher_id_fn
JOIN grades ON subjects.id = grades.subject_id_fn
WHERE  teachers.id = 1
GROUP BY teacher_name, subject_name;
