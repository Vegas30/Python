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

    student_course = relationship('StudentsCourse', back_populates='student')
    courses = relationship('Student', secondary='StudentsCourse', back_populates='students')

class Course(Base):
    __tablename__ = 'courses'

    id = Column(Integer, primary_key=True)
    title = Column(String(60), default=10)
    professor_id = Column(Integer, ForeignKey('professors.id'), nullable= False)

    professor = relationship('Professor', back_populates='course')

    students = relationship('Course', secondary='StudentsCourse', back_populates='courses')
    student_course = relationship('StudentsCourse', back_populates='course')

class StudentsCourse(Base):
    __tablename__ = 'students_courses'
    student_id = Column(Integer, ForeignKey('students.id'), primary_key= True)
    course_id = Column(Integer, ForeignKey('courses.id'), primary_key= True)
    student_course_data = Column(Date, default = date.today())

    student = relationship('Student', back_populates='student_course')
    course = relationship('Course', back_populates='student_course')

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

    student_course1 = StudentsCourse(student = student1, course = course3)
    student_course2 = StudentsCourse(student = student2, course = course3)
    student_course3 = StudentsCourse(student = student3, course = course2)
    student_course4 = StudentsCourse(student = student4, course = course1)
    student_course5 = StudentsCourse(student = student1, course = course2)

    session.add_all([professor1,professor2,student1,student2,student3,student4,student_course1,student_course2,student_course3,student_course4,student_course5])
    session.commit()

except Exception as e:
    session.rollback()
    print(f"Ошибка {e}")

finally:
    session.close()


