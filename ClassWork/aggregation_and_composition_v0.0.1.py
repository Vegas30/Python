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

    def add_course(self, title, teacher):
        course = Course(title, teacher)
        self.courses.append(course)

    def add_teacher(self, teacher):
        self.teachers.append(teacher)

    def add_student(self, student):
        self.students.append(student)

    def add_student_on_course(self, student, course_title):
        for course in self.courses:
            if course.title == course_title:
                student.add_student_on_course(course)

    def get_students_by_teacher(self, teacher_name):
        students_list = []
        for teacher in self.teachers:
            if teacher.name == teacher_name:
                for course in teacher.course_education_teacher:
                    students_list.extend(course.students)
        return students_list

def main():
    school = School()

    teacher1 = Teacher("Максим Николаевич")
    teacher2 = Teacher("Максим Нениколаевич")
    school.add_teacher(teacher1)
    school.add_teacher(teacher2)

    school.add_course("Математика", teacher1)
    school.add_course("Физика", teacher2)

    student1 = Student("Расул")
    student2 = Student("Игорь")
    student3 = Student("Сергей")

    school.add_student(student1)
    school.add_student(student2)
    school.add_student(student3)

    school.add_student_on_course(student1, "Математика")
    school.add_student_on_course(student2, "Математика")

    print([student.name for student in school.get_students_by_teacher("Максим Николаевич")])

if __name__ == "__main__":
    main()
