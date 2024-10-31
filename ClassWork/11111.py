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
        self.course_education = []

    def add_student_on_course(self, course):
        self.course_education.append(course)

class Teacher:
    def __init__(self, name):
        self.name = name
        self.course_education_teacher = []

    def add_course_teacher(self, course):
        self.course_education_teacher.append(course)

class Course:
    def __init__(self, title, teacher):
        self.title = title
        self.teacher = teacher
        teacher.add_course_teacher(self)

class School:
    def __init__(self):
        self.courses = []
        self.teachers = []
        self.students = []

    def add_course(self, title, teacher: Teacher):
        course = Course(title, teacher)
        self.courses.append(course)

    def add_teacher(self, teacher: Teacher):
        self.teachers.append(teacher)

    def add_student(self, student: Student):
        self.students.append(student)

    def add_student_on_course(self, student: Student, course: Course):
        student.add_student_on_course(course)

    def get_student_by_teacher(self, teacher_name):
        for teacher in self.teachers:
            if teacher.name == teacher_name:
                return [student for course in teacher.course_education_teacher for student in self.students if course in student.course_education]

def main():
    school_4 = School()

    teacher1 = Teacher("Максим Николаевич")
    teacher2 = Teacher("Максим Нениколаевич")
    school_4.add_teacher(teacher1)
    school_4.add_teacher(teacher2)

    school_4.add_course("Математика", teacher1)
    school_4.add_course("Физика", teacher2)
    print(teacher1.course_education_teacher)

    student1 = Student("Расул")
    student2 = Student("Игорь")
    student3 = Student("Сергей")

    school_4.add_student(student1)
    school_4.add_student(student2)
    school_4.add_student(student3)

    school_4.add_student_on_course(student1, "Математика")
    school_4.add_student_on_course(student2, "Математика")
    print(student1.course_education)

    print(school_4.get_student_by_teacher("Максим Николаевич"))

if __name__ == "__main__":
    main()
