class Person:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

    def get_info(self) -> str:
        """Возвращает основную информацию о человеке."""
        return f"{self.name}, возраст: {self.age}"


class Student(Person):
    def __init__(self, name: str, age: int, student_id: int):
        super().__init__(name, age)
        self.student_id = student_id
        self.courses = []

    def enroll(self, course: "Course"):
        """Записывает студента на курс, если есть места."""
        if course.add_student(self):
            self.courses.append(course)

    def get_info(self) -> str:
        """Переопределение метода (полиморфизм)."""
        return f"Студент {self.name}, ID: {self.student_id}, Курсы: {[course.title for course in self.courses]}"


class Teacher(Person):
    def __init__(self, name: str, age: int, position: str):
        super().__init__(name, age)
        self.position = position

    def get_info(self) -> str:
        """Переопределение метода (полиморфизм)."""
        return f"Преподаватель {self.name}, должность: {self.position}"


class Assignment:
    def __init__(self, title: str, description: str, max_score: int):
        self.title = title
        self.description = description
        self.max_score = max_score

    def get_info(self) -> str:
        """Возвращает информацию о задании."""
        return f"Задание: {self.title}, Описание: {self.description}, Максимальный балл: {self.max_score}"


class Course:
    def __init__(self, title: str, max_students: int, teacher: Teacher):
        self.title = title
        self.max_students = max_students
        self.teacher = teacher
        self.students = []
        self.assignments = []

    def add_student(self, student: Student) -> bool:
        """Добавляет студента, если есть свободные места."""
        if len(self.students) < self.max_students:
            self.students.append(student)
            return True
        return False

    def create_assignment(self, title: str, description: str, max_score: int):
        """Создает новое задание для курса."""
        assignment = Assignment(title, description, max_score)
        self.assignments.append(assignment)

    def get_info(self) -> str:
        """Возвращает информацию о курсе."""
        assignments_info = "\n".join(assignment.get_info() for assignment in self.assignments)
        return f"Курс: {self.title}, Преподаватель: {self.teacher.name}, Студентов: {len(self.students)} / {self.max_students}\nЗадания:\n{assignments_info}"


class Department:
    def __init__(self, name: str):
        self.name = name
        self.courses = []
        self.teachers = []

    def add_teacher(self, teacher: Teacher):
        """Добавляет преподавателя на кафедру."""
        self.teachers.append(teacher)

    def add_course(self, course: Course):
        """Добавляет курс на кафедру."""
        self.courses.append(course)

    def get_info(self) -> str:
        """Возвращает информацию о кафедре."""
        return f"Кафедра {self.name}: Курсы: {[course.title for course in self.courses]}, Преподаватели: {[teacher.name for teacher in self.teachers]}"


cs_department = Department("Кафедра информатики")

teacher1 = Teacher("Александр Сергеевич", 45, "Лектор")
teacher2 = Teacher("Мария Ивановна", 38, "Ассистент")

cs_department.add_teacher(teacher1)
cs_department.add_teacher(teacher2)

course1 = Course("Алгоритмы и структуры данных", 2, teacher1)
course2 = Course("Основы программирования", 3, teacher2)

cs_department.add_course(course1)
cs_department.add_course(course2)

student1 = Student("Иван", 20, 101)
student2 = Student("Анна", 19, 102)
student3 = Student("Дмитрий", 21, 103)

student1.enroll(course1)
student2.enroll(course1)
student3.enroll(course2)

course1.create_assignment("Задание 1", "Реализовать алгоритм сортировки", 100)
course1.create_assignment("Задание 2", "Написать программу, используя стек", 80)

course2.create_assignment("Задание 1", "Написать программу на Python", 50)

print(cs_department.get_info())
print(course1.get_info())
print(course2.get_info())
print(student1.get_info())
print(student2.get_info())
print(student3.get_info())

