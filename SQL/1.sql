-- 1. Выбрать все отделы:
-- select nameOtdel from departments; 
-- 2. Выбрать всех преподавателей:
-- SELECT teachers.name, teachers.otchestvo, teachers.surname FROM teachers
-- 8. Выбрать имена и должности всех преподавателей:
-- SELECT teachers.name, teachers.post from teachers 
-- 9. Выбрать имена отделов и их начальников:
-- SELECT departments.nameOtdel, departments.bossOtdel FROM departments;
-- 10. Выбрать имена и специализации всех студентов:
-- SELECT name, nameSpecial FROM students JOIN specializations ON special_id = idSpecial;
-- 11. Выбрать имена студентов и их адреса:
-- SELECT name, adress FROM students;
-- 13. Выбрать имена преподавателей и названия их уроков: 
SELECT 
    name, nameLessons
FROM
    teachers
        JOIN
    lessons ON idTeachers = teacher_id;
-- 14. Выбрать имена и должности всех преподавателей, у которых номер телефона начинается с "8":
SELECT name, post
FROM teachers
WHERE phone LIKE '8%';
-- 15. Выбрать имена студентов, у которых регион равен 2:
-- 16. Выбрать имена студентов и названия их специализаций, у которых номер телефона начинается с "9":
-- 17. Выбрать имена отделов, в которых работает босс с фамилией "Иванов":
-- 18. Выбрать имена всех студентов в порядке убывания их имен:
SELECT name
FROM students
order by name DESC;
-- 19. Выбрать среднюю оценку по всем тестам:
-- 20. Выбрать количество студентов в каждом регионе:
-- 21. Обновить должность преподавателя с id 5 на "Доцент":
-- 22. Добавить нового студента: