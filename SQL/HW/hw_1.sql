-- 1. Выбрать все отделы: 
SELECT 
    nameOtdel
FROM
    departments; 
-- 2. Выбрать всех преподавателей:
SELECT 
    *
FROM
    teachers;
-- 8. Выбрать имена и должности всех преподавателей:
SELECT 
    name, post
FROM
    teachers;
-- 9. Выбрать имена отделов и их начальников:
SELECT 
    nameOtdel, bossOtdel
FROM
    departments;
-- 10. Выбрать имена и специализации всех студентов:
SELECT 
    name, nameSpecial
FROM
    students
        JOIN
    specializations ON special_id = idSpecial; 
-- 11. Выбрать имена студентов и их адреса: 
SELECT 
    name, adress
FROM
    students;
-- 13. Выбрать имена преподавателей и названия их уроков: 
SELECT 
    name, nameLessons
FROM
    teachers
        JOIN
    lessons ON idTeachers = teacher_id; 
-- 14. Выбрать имена и должности всех преподавателей, у которых номер телефона начинается с "8": 
SELECT 
    name, post
FROM
    teachers
WHERE
    phone LIKE '8%';
-- 15. Выбрать имена студентов, у которых регион равен 2:
SELECT 
    name
FROM
    students
WHERE
    region = 2;
-- 16. Выбрать имена студентов и названия их специализаций, у которых номер телефона начинается с "9": 
SELECT 
    name, specializations.nameSpecial
FROM
    students
        JOIN
    specializations ON special_id = idSpecial
WHERE
    students.number LIKE '9%';
-- 17. Выбрать имена отделов, в которых работает босс с фамилией "Иванов":
SELECT 
    nameOtdel
FROM
    departments
WHERE
    departments.bossOtdel LIKE 'Иванов %';  
-- 18. Выбрать имена всех студентов в порядке убывания их имен: 
SELECT 
    name
FROM
    students
ORDER BY name DESC;
-- 19. Выбрать среднюю оценку по всем тестам: 
SELECT 
    AVG(ball) AS average_ball
FROM
    tests;
-- 20. Выбрать количество студентов в каждом регионе: 
SELECT 
    region, COUNT(*) AS num_students
FROM
    students
GROUP BY region;
-- 21. Обновить должность преподавателя с id 5 на "Доцент":
UPDATE teachers 
SET 
    post = 'Доцент'
WHERE
    idTeachers = 5;
-- 22. Добавить нового студента:
INSERT INTO test.students (idStudent, surname, name, adress, city, region, number, special_id) 
VALUES ('31', 'Добавлялов', 'Новичок', 'ул. Новая, д.1', 'Астрахань', '30', '892711111', '11');
-- delete from students where idStudent = 31;