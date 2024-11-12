# Инкапсуляция + Агрегация
# Создайте классы University, Faculty, и Professor. University будет
# иметь список факультетов, а каждый факультет будет содержать список
# преподавателей.
# Требования:
# 1. Класс Professor инкапсулирует информацию о преподавателе, такую
# как имя и специальность.
# 2. Класс Faculty содержит список преподавателей (инкапсуляция) и
# предоставляет доступ к добавлению и удалению преподавателей
# через методы.
# 3. Класс University содержит факультеты как отдельные объекты
# (агрегация).
# —------------------------------------------
# prof1 = Professor("Alice", "Computer Science")
# prof2 = Professor("Bob", "Mathematics")
# faculty1 = Faculty("Engineering")
# faculty1.add_professor(prof1)
# faculty1.add_professor(prof2)
# university = University("Tech University")
# university.add_faculty(faculty1)
# university.list_faculties()
# faculty1.list_professors()
# faculty1.remove_professor("Alice")
# faculty1.list_professors()
# —--------------------------------------------------
# Результат:
# Преподаватель 'Alice' добавлен на факультет 'Engineering'
# Преподаватель 'Bob' добавлен на факультет 'Engineering'
# Факультет 'Engineering' добавлен в университет 'Tech University'
# Факультеты университета 'Tech University':
# - Engineering
# Преподаватели факультета 'Engineering':
# - Professor Alice, Specialty: Computer Science
# - Professor Bob, Specialty: Mathematics
# Преподаватель 'Alice' удален с факультета 'Engineering'
# Преподаватели факультета 'Engineering':
# - Professor Bob, Specialty: Mathematics

class Professor:
    def __init__(self, name, specialty):
        self.__name = name
        self.__specialty = specialty

    @property
    def name(self):
        return self.__name

    def get_info(self):
        return f"Преподаватель {self.__name}, {self.__specialty}"


class Faculty:
    def __init__(self, faculty_name):
        self.__faculty_name = faculty_name
        self.__professors = []

    @property
    def faculty_name(self):
        return self.__faculty_name

    def add_professor(self, professor):
        self.__professors.append(professor)
        print(f"Преподаватель {professor.name} добавлен на факультет {self.__faculty_name}")

    def remove_professor(self, professor_name):
        for professor in self.__professors:
            if professor.name == professor_name:
                self.__professors.remove(professor)
                print(f"Преподаватель {professor.name} уволен с факультета {self.__faculty_name}")
                return
        print(f"Преподаватель {professor_name} не найден в факультете {self.__faculty_name}")

    def list_professors(self):
        print(f"Преподаватели факультета {self.__faculty_name}")
        for professor in self.__professors:
            print(f"- {professor.get_info()}")


class University:
    def __init__(self, university_name):
        self.__university_name = university_name
        self.__faculties = []

    def add_faculty(self, faculty):
        self.__faculties.append(faculty)
        print(f"Факультет {faculty.faculty_name} добавлен в университет {self.__university_name}")


def main():
    prof1 = Professor("МН", "Python")
    prof2 = Professor("Расул", "Базы данных")

    faculty1 = Faculty("ITTT")
    faculty1.add_professor(prof1)
    faculty1.add_professor(prof2)

    university = University("University M.N.")
    university.add_faculty(faculty1)

    faculty1.list_professors()

    faculty1.remove_professor("Расул")
    faculty1.list_professors()


main()
