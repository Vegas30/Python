#1. Создать класс Person, который имеет атрибуты: имя, возраст и город проживания.
#Напишите метод, который выводит информацию о человеке.

class Person:
    def __init__(self, name, age, city):
        self.name1 = name
        self.age = age
        self.tall = city

    def info_person(self):
        print(f"Его зовут {self.name1} ему лет {self.age} и живет он в {self.tall}")

def main():
    person = Person(input("Введите имя пользователя"), int(input("Введите возраст")), 'Астрахань')
    person2 = Person(input("Введите имя пользователя"), int(input("Введите возраст")), 'Астрахань')
    person.info_person()

main()


#2. Создайте два класса: Student и Course. Класс Student должен иметь атрибуты:
#имя и список курсов, на которые он записан. Класс Course должен содержать информацию
# о названии курса и максимальном количестве студентов. Реализуйте возможность добавления
# студента на курс, если есть свободные места.

class Student:
    def __init__(self,name):
        self.name = name
        self.courses = []

    def get_courses(self):
        return [course for course in self.courses]
class Course:
    def __init__(self,name, max_students):
        self.name = name
        self.max_students = max_students
        self.students = []

    def add_student(self, student):
        if len(self.students) < self.max_students:
            self.students.append(student)
            student.courses.append(self.name)
            print(f"Студент с именем {student.name} добавлен на курс {self.name}")
        else:
            print(f"Курс {self.name} переполнен!")

    def get_students(self):
        return [student.name for student in self.students]

def main():
    name = input("Введите имя курса: ")
    max_students = int(input("Введите количество студентов"))
    course_math = Course(name, max_students)
    course_biology = Course('bio', 25)

    student1 = Student("Maxim")
    student2 = Student("Igor")
    student3 = Student("Masha")

    course_math.add_student(student1)
    course_biology.add_student(student1)
    course_math.add_student(student2)
    course_biology.add_student(student3)

    print(f"Курсы на которая учится {student1.name} - {student1.get_courses()}")
    print(f"Cтуденты курса {course_math.name} - {course_math.get_students()}")
main()
