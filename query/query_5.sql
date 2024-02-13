SELECT teachers.fullname AS name, subjects.name AS subject_name
FROM subjects
JOIN teachers ON subjects.teacher_id_fn = teachers.id
WHERE teachers.id = 3;
