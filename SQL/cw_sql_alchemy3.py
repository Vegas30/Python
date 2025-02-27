from sqlalchemy.orm import declarative_base, sessionmaker, relationship
from sqlalchemy import Integer, Column, String, ForeignKey, Date, create_engine
from datetime import date
Base = declarative_base()


class Professor(Base):
    __tablename__ = 'professors'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)

    course = relationship('Course', back_populates= 'professor')

class Student(Base):
    __tablename__ = 'students'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)

    courses = relationship('Course', secondary='students_courses', back_populates='students')

class Course(Base):
    __tablename__ = 'courses'

    id = Column(Integer, primary_key=True)
    title = Column(String(60), default=10)
    professor_id = Column(Integer, ForeignKey('professors.id'), nullable= False)

    professor = relationship('Professor', back_populates='course')

    students = relationship('Student', secondary='students_courses', back_populates='courses')

class StudentsCourse(Base):
    __tablename__ = 'students_courses'
    student_id = Column(Integer, ForeignKey('students.id'), primary_key= True)
    course_id = Column(Integer, ForeignKey('courses.id'), primary_key= True)
    student_course_data = Column(Date, default=date.today)


engine = create_engine('postgresql://postgres:12345678@localhost:5433/courses_manager')
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

session.begin()
try:
    professor1 = Professor(name="Rasul")
    professor2 = Professor(name="Igor")

    course1 = Course(title="Логическое проектирование", professor=professor1)
    course2 = Course(title="Дизайн", professor=professor2)
    course3 = Course(title="Data Science", professor=professor1)

    student1 = Student(name="Sergey")
    student2 = Student(name="Dmitriy")
    student3 = Student(name="Pavel")
    student4 = Student(name="Sergey")

    student1.courses.extend([course3,course2])
    student2.courses.append(course3)
    student3.courses.append(course1)
    student4.courses.append(course2)

    session.add_all([professor1,professor2,student1,student2,student3,student4])
    session.commit()

    sergey = session.query(Student).filter_by(name="Sergey").first()
    print(f"Курсы студента {sergey.name}: ")
    for course in sergey.courses:
        print(f"- {course.title} (Преподаватель: {course.professor.name})")

    data_science = session.query(Course).filter_by(title="Data Science").first()
    print(f"\nCтуденты записанные на курс {data_science.title}")
    for student in data_science.students:
        print(f"- {student.name}")


except Exception as e:
    session.rollback()
    print(f"Ошибка {e}")

finally:
    session.close()


