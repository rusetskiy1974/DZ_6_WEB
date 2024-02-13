SELECT students.fullname AS name, subjects.name AS  subject_name, grades.grade_date AS data
FROM students
JOIN grades ON students.id = grades.student_id_fn
JOIN subjects ON grades.subject_id_fn  = subjects.id
WHERE students.id = 6
ORDER BY data ;
