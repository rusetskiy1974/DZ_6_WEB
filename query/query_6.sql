SELECT groups.name AS group_name,  students.fullname AS student_name
FROM students
JOIN groups ON students.group_id_fn  = groups.id
WHERE groups.id = 2;
