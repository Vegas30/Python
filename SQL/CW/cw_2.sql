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
SELECT nameLessons FROM lessons JOIN teachers ON idTeachers = teacher_id WHERE surname LIKE 'Петров';
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
-- 40. Выбрать имена всех преподавателей, проводивших уроки с аудиторией больше 2:
SELECT concat(t.name,' ', t.surname) as full_name, l.audition
FROM teachers as t
JOIN lessons as l
ON t.idTeachers = l.teacher_id 
WHERE l.audition > 2;
-- 41. Найти все уроки, проведенные преподавателем с именем "Анна" или "Иван":
select nameLessons from lessons join teachers on teacher_id = idTeachers where name = 'Анна' or name = 'Иван';
select nameLessons from lessons join teachers on teacher_id = idTeachers where name IN ('Анна','Иван');
-- 42. Найти все специализации, в названии которых есть слово "IT": ???!!! нет ни одной
select * from specializations where nameSpecial like 'Ин%';
-- 46. Выбрать все уроки, проведенные преподавателем с фамилией "Смирнов" и аудитория которых менее или равна 2:
select l.nameLessons, concat_ws(' ', t.name, t.otchestvo, t.surname) as ful_name
from lessons as l
join teachers as t
ON teacher_id = idTeachers
where t.surname = 'Смирнов' and l.audition <= 2;
-- 48. Найти все тесты, на которых было не менее 2 студентов:
select t.idTest, t.nameTest, count(r.student_id) as student_amount
from tests as t
join result as r ON t.idTest = r.tests_id
group by t.idTest, t.nameTest
having  student_amount >= 2;
-- 49. Найти количество уникальных специализаций среди студентов: ??? Не понял вопроса
SELECT count(distinct students.special_id) as UniqSpec_Num FROM students;
-- 51. Найти всех студентов, проживающих в городе "Санкт-Петербург" и у которых номер дома больше 100:
SELECT s.name, s.city, cast(trim(trim(LEADING '.' FROM right(adress, 3))) as signed) as house_number
from students as s
having city = 'Санкт-Петербург' AND house_number > 100;

-- 52. Посчитать количество студентов в каждом городе:
select city, count(*) as StudentCount
FROM students
group by city;
-- 61. Найти все отделы, в которых руководителем является преподаватель с фамилией "Иванов":
select d.nameOtdel from departments as d where bossOtdel LIKE 'Иванов %';
-- 63. Посчитать количество уроков для каждого преподавателя:
select concat_ws(' ', surname, name, otchestvo) as full_name, count(teacher_id) AS lessons_count
from teachers
join lessons ON idTeachers = teacher_id
group by idTeachers;
-- 64. Найти все специализации, на которых учатся студенты из города "Москва":
select concat_ws(' ', name, surname) as full_name, city, nameSpecial from students join specializations ON special_id = idSpecial where city = 'Москва';
-- 73. Посчитать общее количество тестов, проведенных по каждому предмету:
select l.nameLessons, count(t.idTest) as tests_count
from lessons as l
join tests as t on idLessons = lesson_id
group by idLessons, nameLessons;
-- 74. Найти всех студентов, чьи фамилии содержат букву "е" и имеют длину не менее 5 символов:
select * from students where surname LIKE '%е%' and character_length(surname) > 8;
-- 75. Обновить данные о пройденных тестах: установить значение "Пройден" для всех тестов, на которых студенты получили оценку выше 3:
UPDATE tests as t
SET t.proiden = 'Пройден'
WHERE t.idTest IN (SELECT r.tests_id from result as r where r.ocenka > 3 ) ;
-- 77. Посчитать количество студентов, зарегистрированных на каждый специализационный курс:
select special_id, l.nameLessons, count(idStudent) as studeny_amount
from students as s
join lessons as l
ON special_id = idLessons
group by special_id;
-- 73. Посчитать количество преподавателей в каждом отделе:
select t.departments_id, d.nameOtdel, count(t.idTeachers) as teachers_amount
from teachers as t
join departments as d
ON departments_id = idDepartments
group by departments_id;
-- 75. Обновить данные о специализации студента с именем "Иван" и фамилией "Иванов":
UPDATE students
SET students.special_id = '20'
WHERE students.name = 'Иван' and students.surname = 'Иванов';
-- 78. Посчитать количество студентов в каждом городе:
SELECT s.city, count(s.idStudent) as students_amount
FROM students as s
group by s.city;
-- 79. Найти все тесты, на которых получены оценки от 4 до 5:
select t.idTest, t.nameTest, r.ocenka 
from tests as t
join result as r
on t.idTest = r.tests_id
where r.ocenka between 4 and 5;
-- 81. Найти всех студентов, чьи фамилии начинаются на "П" и которые изучают специализацию "Физика":
SELECT concat_ws(' ', st.name, st.surname) as full_name, spec.nameSpecial 
FROM students as st
JOIN specializations as spec
ON st.special_id = spec.idSpecial
where st.surname LIKE 'П%' and spec.nameSpecial = 'Физика';