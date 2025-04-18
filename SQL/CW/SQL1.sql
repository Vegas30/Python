 -- Выбрать все записи из таблицы "students", где фамилия начинается с буквы "А"
 -- SELECT * FROM students WHERE surname LIKE 'А%';
 -- Выбрать имена всех студентов, у которых номер телефона не начинается с "8"
 -- SELECT * FROM students WHERE number NOT IN(8);
 --  Выбрать все уроки, проведенные преподавателем с фамилией "Петров"
 -- SELECT nameLessons FROM lessons JOIN teachers ON idTeachers = teacher_id WHERE surname LIKE 'Петров';
 -- Выбрать количество студентов в каждом городе
 -- SELECT city, COUNT(idStudent) AS student_count FROM students GROUP BY city;
 -- Выбрать все тесты, на которых не было ни одного студента
 --  SELECT * FROM tests WHERE idTest NOT IN (SELECT tests_id FROM result);
 -- Обновить специализацию студента с фамилией "Сидоров" на "Программирование":
-- UPDATE students SET special_id = (SELECT idSpecial FROM specializations WHERE nameSpecial = 'Программирование') WHERE surname = 'Сидоров';
-- 39. Выбрать имена всех студентов, у которых оценка по тестам выше 80:
-- SELECT * FROM students WHERE idStudent = ALL (SELECT student_id From result WHERE ocenka > '80');
-- 40. Выбрать имена всех преподавателей, проводивших уроки с аудиторией больше 30:
 -- ?
-- 41. Найти все уроки, проведенные преподавателем с именем "Анна" или "Иван":

 -- SELECT nameLessons FROM lessons WHERE teacher_id IN (SELECT idTeachers FROM teachers WHERE name IN ('Анна') OR ('Иван'));
-- 42. Найти все специализации, в названии которых есть слово "IT":

-- SELECT * FROM specializations WHERE nameSpecial IN( 'IT');
-- 46. Выбрать все уроки, проведенные преподавателем с фамилией "Смирнов" и аудитория которых менее или равна 20:
-- SELECT * FROM lessons WHERE teacher_id = (SELECT idTeachers FROM teachers WHERE surname = 'Смирнов') AND audition <= '20';
-- 48. Найти все тесты, на которых было не менее 10 студентов:
-- SELECT * FROM tests WHERE idTest > ALL(SELECT tests_id FROM result WHERE student_id > 10);
-- 49. Найти количество уникальных специализаций среди студентов:
-- SELECT nameSpecial, COUNT(DISTINCT idSpecial) AS unique_count FROM specializations WHERE idSpecial 
-- IN (SELECT  DISTINCT special_id FROM students) GROUP BY nameSpecial;
-- 51. Найти всех студентов, проживающих в городе "Санкт-Петербург" и у которых номер дома больше 100:
-- ?
-- 52. Посчитать количество студентов в каждом городе:
-- SELECT city, COUNT(idStudent) AS count_students FROM students GROUP BY city;
-- 61. Найти все отделы, в которых руководителем является преподаватель с фамилией "Иванов":
-- SELECT nameOtdel FROM departments WHERE bossOtdel LIKE 'Иванов %';
-- 63. Посчитать количество уроков для каждого преподавателя:
-- SELECT teacher_id, COUNT(idLessons) AS количество_уроков FROM lessons GROUP BY teacher_id;
-- 64. Найти все специализации, на которых учатся студенты из города "Москва":
-- SELECT nameSpecial FROM specializations WHERE idSpecial = (SELECT special_id FROM students WHERE city = 'Москва');
-- 73. Посчитать общее количество тестов, проведенных по каждому предмету:
-- SELECT lesson_id, COUNT(idTest) AS Количество_тестов FROM tests GROUP BY lesson_id;
-- 74. Найти всех студентов, чьи фамилии содержат букву "е" и имеют длину не менее 5 символов:
--  SELECT * FROM students WHERE (surname LIKE '%е%') AND (surname LIKE '_____');
-- 75. Обновить данные о пройденных тестах: установить значение "Пройден" для всех тестов, на которых студенты получили оценку выше 3:
-- UPDATE tests SET proiden = 'Пройден' WHERE idTest = ANY (SELECT tests_id FROM result WHERE ocenka > 3);
-- 77. Посчитать количество студентов, зарегистрированных на каждый специализационный курс:
-- SELECT nameSpecial, (SELECT COUNT(*) FROM students WHERE special_id = idSpecial) AS количество_студентов FROM specializations;
-- 73. Посчитать количество преподавателей в каждом отделе:
-- SELECT nameOtdel, (SELECT COUNT(*) FROM teachers WHERE departments_id = idDepartments) AS количество_преподавателей FROM departments;
-- SELECT nameOtdel, COUNT(idTeachers) FROM departments LEFT JOIN teachers ON idDepartments = departments_id GROUP BY idDepartments;
-- 75. Обновить данные о специализации студента с именем "Иван" и фамилией "Иванов":
-- UPDATE students SET special_id = '11' WHERE name = 'Иван' AND surname = 'Иванов';
-- 78. Посчитать количество студентов в каждом городе:
-- SELECT city, COUNT(idStudent) AS количество_студентов FROM students GROUP BY city;
-- 79. Найти все тесты, на которых получены оценки от 4 до 5:
-- SELECT nameTest FROM tests WHERE idTest = ANY (SELECT tests_id FROM result WHERE ocenka BETWEEN 4 AND 5);
-- 81. Найти всех студентов, чьи фамилии начинаются на "П" и которые изучают специализацию "Физика":
-- SELECT * FROM students WHERE surname LIKE 'П%' AND special_id = (SELECT idSpecial FROM specializations WHERE nameSpecial = 'Физика');
