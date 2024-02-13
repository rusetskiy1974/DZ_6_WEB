SELECT groups.name AS group_name, s.fullname AS student_name, grades.grade, grades.grade_date
FROM students s
JOIN groups ON s.group_id_fn = groups.id
JOIN grades  ON s.id = grades.student_id_fn
JOIN subjects ON grades.subject_id_fn = subjects.id
WHERE groups.id = 2
AND subjects.id = 2
AND grades.grade_date = (
    SELECT MAX(grade_date)
    FROM grades
    WHERE subject_id_fn = subjects.id
);
