-- 30. Выбрать все записи из таблицы "students", где фамилия начинается с буквы "А"
SELECT 
    *
FROM
    students
WHERE
    surname LIKE 'А%';
-- 31. Выбрать имена всех студентов, у которых номер телефона не начинается с "8":
SELECT 
    name
FROM
    students
WHERE
    number LIKE '8%';
-- 32. Выбрать все уроки, проведенные преподавателем с фамилией "Петров":
select nameLessons from lessons where teacher_id = 1;
-- 33. Выбрать количество студентов в каждом городе:
SELECT city, COUNT(*) AS num_students
FROM students
group by city;
-- 34. Выбрать все тесты, на которых не было ни одного студента:
SELECT * FROM tests WHERE idTest NOT IN (SELECT tests_id FROM result);
-- Обновить специализацию студента с фамилией "Сидоров" на "Программирование":
update students
SET special_id = '1'
where students.surname = 'Сидоров';
-- 39. Выбрать имена всех студентов, у которых оценка по тестам выше 80:
select name from students join tests on special_id = tests.lesson_id where ball > 80;
-- 40. Выбрать имена всех преподавателей, проводивших уроки с аудиторией больше 30: ???!!!

-- 41. Найти все уроки, проведенные преподавателем с именем "Анна" или "Иван":
select nameLessons from lessons join teachers on teacher_id = idTeachers where name = 'Анна' or name = 'Иван';
select nameLessons from lessons join teachers on teacher_id = idTeachers where name IN ('Анна','Иван');
-- 42. Найти все специализации, в названии которых есть слово "IT": ???!!! нет ни одной

-- 46. Выбрать все уроки, проведенные преподавателем с фамилией "Смирнов" и аудитория которых менее или равна 20: ???!!!

-- 48. Найти все тесты, на которых было не менее 10 студентов: ???!!!

-- 49. Найти количество уникальных специализаций среди студентов: ???!!! EXCEPT - не работает? Не понял вопроса
SELECT count(distinct students.special_id) as UniqSpec_Num FROM students;
-- 51. Найти всех студентов, проживающих в городе "Санкт-Петербург" и у которых номер дома больше 100:
-- SELECT name, right(adress, 3) as house_number from students; --  where city = 'Санкт-Петербург' AND house_number > 100);

select name, substr(adress FROM 'д. ') as house_number from students;

SELECT name, COUNT(*) AS house_number
FROM teachers
GROUP BY departments_id
HAVING num_teachers > 5;


-- SELECT *
-- FROM students
-- WHERE surname = 'Кузьмина' 
-- AND region > (
--     SELECT AVG(region)
--     FROM students
-- );

-- 52. Посчитать количество студентов в каждом городе:
select city, count(*) as StudentCount
FROM students
group by city;
-- 61. Найти все отделы, в которых руководителем является преподаватель с фамилией "Иванов":
select departments.nameOtdel from departments where bossOtdel LIKE 'Иванов %';
-- 63. Посчитать количество уроков для каждого преподавателя:
select concat_ws(' ', surname, name, otchestvo) as full_name, count(teacher_id) AS lessons_count
from teachers
join lessons ON idTeachers = teacher_id
group by idTeachers;
-- 64. Найти все специализации, на которых учатся студенты из города "Москва":
select concat_ws(' ', name, surname) as full_name, city, nameSpecial from students join specializations ON special_id = idSpecial where city = 'Москва';
-- 73. Посчитать общее количество тестов, проведенных по каждому предмету: ???!!! Считает красиво но не правильно
select nameLessons, count(lesson_id) as tests_count
from lessons
join tests on idLessons = lesson_id
group by nameLessons;
-- 74. Найти всех студентов, чьи фамилии содержат букву "е" и имеют длину не менее 5 символов:
select * from students where surname LIKE '%е%' and character_length(surname) > 8;
-- 75. Обновить данные о пройденных тестах: установить значение "Пройден" для всех тестов, на которых студенты получили оценку выше 3:

-- 77. Посчитать количество студентов, зарегистрированных на каждый специализационный курс:
-- 73. Посчитать количество преподавателей в каждом отделе:
-- 75. Обновить данные о специализации студента с именем "Иван" и фамилией "Иванов":
-- 78. Посчитать количество студентов в каждом городе:
-- 79. Найти все тесты, на которых получены оценки от 4 до 5:
-- 81. Найти всех студентов, чьи фамилии начинаются на "П" и которые изучают специализацию "Физика":