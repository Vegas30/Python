class ValidationError(Exception):
    """Кастомное исключение для проверки данных."""
    def __init__(self, message):
        super().__init__(message)


class PrintableMixin:
    """Миксин для предоставления текстового представления объекта."""
    def __str__(self):
        attrs = ", ".join(f"{k}={v}" for k, v in self.__dict__.items())
        return f"{self.__class__.__name__}({attrs})"


class LoggingMixin:
    """Миксин для логирования операций."""
    def log_action(self, action: str):
        print(f"[LOG] {self.__class__.__name__}: {action}")


class Person(PrintableMixin):
    """Абстрактный базовый класс для всех людей."""
    def __init__(self, name: str, age: int):
        if not name:
            raise ValidationError("Имя не может быть пустым.")
        if age <= 0:
            raise ValidationError("Возраст должен быть положительным числом.")
        self.name = name
        self.age = age

    def introduce(self):
        """Абстрактный метод, который должен быть реализован в подклассах."""
        raise NotImplementedError("Метод introduce() должен быть реализован.")


class Teacher(Person, LoggingMixin):
    """Класс Преподаватель с логированием."""
    def __init__(self, name: str, age: int, salary: float):
        super().__init__(name, age)
        self.salary = salary
        self.log_action(f"Создан преподаватель {name} с зарплатой {salary}")

    def introduce(self):
        return f"Я преподаватель. Меня зовут {self.name}, мне {self.age} лет."

    @classmethod
    def from_experience(cls, name: str, experience: int):
        """Создание учителя с расчетом возраста по опыту."""
        age = 22 + experience
        salary = 50000 + experience * 2000
        return cls(name=name, age=age, salary=salary)


class Student(Person, LoggingMixin):
    """Класс Студент."""
    def __init__(self, name: str, age: int):
        super().__init__(name, age)
        self.courses = []
        self.log_action(f"Создан студент {name}")

    def add_course(self, course: str):
        """Добавляет курс студенту."""
        self.courses.append(course)
        self.log_action(f"Студент {self.name} записан на курс {course}")

    def introduce(self):
        return f"Я студент. Меня зовут {self.name}, мне {self.age} лет."


class OnlineLearningMixin:
    """Миксин для предоставления онлайн-обучения."""
    def teach_online(self):
        return f"{self.name} проводит урок онлайн."


class OnlineTeacher(Teacher, OnlineLearningMixin):
    """Преподаватель, который проводит онлайн-занятия."""
    def introduce(self):
        return f"Я онлайн-преподаватель. Меня зовут {self.name}, мне {self.age} лет."


class Course(PrintableMixin):
    """Класс для представления курса."""
    def __init__(self, title: str):
        self.title = title
        self.students = []

    def enroll(self, student: Student):
        """Зачисление студента на курс."""
        self.students.append(student)

    def __len__(self):
        return len(self.students)

    def __getitem__(self, index):
        return self.students[index]


class University(PrintableMixin, LoggingMixin):
    """Класс Университет."""
    def __init__(self, name: str):
        self.name = name
        self.teachers = []
        self.courses = []
        self.log_action(f"Университет {name} создан")

    def add_teacher(self, teacher: Teacher):
        self.teachers.append(teacher)
        self.log_action(f"Добавлен преподаватель {teacher.name}")

    def add_course(self, course: Course):
        self.courses.append(course)
        self.log_action(f"Добавлен курс {course.title}")


def explore_class(cls):
    """Демонстрирует использование __mro__ и __dict__."""
    print(f"Иерархия классов ({cls.__name__}):", cls.__mro__)
    print("Атрибуты и методы класса:")
    print(cls.__dict__)


if __name__ == "__main__":
    try:
        student1 = Student(name="Иван", age=20)
        student2 = Student(name="Мария", age=22)
        teacher1 = Teacher(name="Пётр", age=40, salary=75000)
        teacher2 = OnlineTeacher(name="Елена", age=35, salary=80000)

        python_course = Course(title="Python для начинающих")
        python_course.enroll(student1)
        python_course.enroll(student2)

        university = University(name="Tech Academy")
        university.add_teacher(teacher1)
        university.add_teacher(teacher2)
        university.add_course(python_course)

        print(teacher1.introduce())
        print(teacher2.introduce())
        print(teacher2.teach_online())

        print(f"Курс: {python_course.title}, количество студентов: {len(python_course)}")

        explore_class(OnlineTeacher)

    except ValidationError as e:
        print(f"Ошибка валидации: {e}")
