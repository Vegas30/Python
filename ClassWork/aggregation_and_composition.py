# Создайте систему для онлайн-школы, состоящую из классов Student, Course, Teacher, и School.
#
# Класс Student:
#
# Хранит информацию о студенте (например, имя).
# Содержит список курсов, на которые записан студент.
# Не может существовать без курса.
# Класс Course:
#
# Содержит название курса и ссылку на преподавателя (Teacher), который его ведёт.
# Содержит список студентов, записанных на курс.
# Не может существовать без студентов.
# Класс Teacher:
#
# Хранит информацию о преподавателе (например, имя).
# Содержит список курсов, которые он преподаёт.
# Не может существовать без курса.
# Класс School:
#
# Хранит список студентов и список преподавателей.
# Позволяет записывать студентов на курсы.
# Метод get_students_by_teacher, который возвращает список студентов, посещающих курсы конкретного преподавателя.
# Требования:
#
# Создайте метод enroll_student в классе School, который будет записывать студента на курс.
# Создайте метод get_students_by_teacher, который будет возвращать список студентов для указанного преподавателя.

class Student:
    def __init__(self, name):
        self.name = name
        self.courses = []

class Course:
    def __init__(self, name, teacher):
        self.name = name
        self.teacher = teacher
        self.students = []

class Teacher:
    def __init__(self, name):
        self.name = name
        self.courses = []

class School:
    def __init__(self):
        self.students = []
        self.teachers = []

    def enroll_student(self, student, course):
        if student not in course.students:
            course.students.append(student)
            student.courses.append(course)

    def get_students_by_teacher(self, teacher):
        students_list = []
        for course in teacher.courses:
            students_list.extend(course.students)
        return students_list

# Пример использования
# Создание объектов студентов, преподавателей и курсов
student1 = Student("Alice")
student2 = Student("Bob")
teacher1 = Teacher("Mr. Smith")
course1 = Course("Math", teacher1)
course2 = Course("Science", teacher1)

# Создание объекта школы
school = School()

# Запись студентов на курсы
school.enroll_student(student1, course1)
school.enroll_student(student2, course1)
school.enroll_student(student2, course2)

# Получение списка студентов для конкретного преподавателя
students_by_teacher1 = school.get_students_by_teacher(teacher1)
for student in students_by_teacher1:
    print(student.name)
