SELECT s.fullname AS student_name, groups.name, subjects.name, grades.grade, grades.grade_date
FROM students s
JOIN groups ON s.group_id_fn = groups.id
JOIN grades ON s.id = grades.student_id_fn
JOIN subjects ON grades.subject_id_fn  = subjects.id
WHERE groups.id = 1 AND subjects.id = 2;
