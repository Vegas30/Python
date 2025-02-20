from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker

# Создание базового класса
Base = declarative_base()


# Определение модели
class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String)


# Создание подключения к базе данных
engine = create_engine('postgresql://postgres:12345678@localhost:5434/Python_41')
Base.metadata.create_all(engine)

# Создание сессии
Session = sessionmaker(bind=engine)
session = Session()

# Открываем транзакцию вручную
session.begin()

try:
    # Добавление нового пользователя
    user = User(name="Alice")
    session.add(user)

    # Коммит изменений
    session.commit()
except Exception as e:
    # Если произошла ошибка, откатываем изменения
    session.rollback()
    print(f"Ошибка: {e}")

# Закрытие сессии
session.close()
