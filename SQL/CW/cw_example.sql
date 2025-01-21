SELECT idTeachers AS id, CONCAT(surname, ' ', name) AS full_name, 'Teacher' AS role
FROM teachers
UNION ALL
SELECT idStudent AS id, CONCAT(surname, ' ', name) AS full_name, 'Student' AS role
FROM students;

INSERT INTO departments (nameOtdel, bossOtdel)
VALUES('Отдел качества', 'Петров Петр Петрович');

select * FROM departments;

SELECT DISTINCT nameOtdel FROM departments;


UPDATE teachers
SET post = 'Главный преподаватель'
WHERE surname  = 'Иванов';

select ball * 12 AS annual_ball FROM tests;
SELECT avg(ball) AS annual_ball FROM tests;

SELECT name AS teacher_name, nameOtdel AS department_name
FROM teachers
INNER JOIN departments ON departments_id = idDepartments;

SELECT *
FROM departments
LEFT JOIN teachers ON idDepartments = departments_id;

SELECT *
FROM departments
RIGHT JOIN teachers ON idDepartments = departments_id;


-- SELECT name FROM students 
-- INTERSECT
-- SELECT name FROM teachers;


SELECT departments_id, COUNT(*) AS num_teachers
FROM teachers
GROUP BY departments_id
HAVING num_teachers > 5;  

SELECT * FROM students WHERE region IN (18, 19, 20);
