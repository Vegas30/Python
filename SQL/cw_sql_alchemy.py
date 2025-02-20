import sqlalchemy
import psycopg2

from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Integer, String, Float, Date, ForeignKey

engine = create_engine('postgresql://postgres:12345678@localhost:5434/Python_41')

Base = declarative_base()


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    age = Column(Integer)


class Product(Base):
    __tablename__ = 'products'
    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    price = Column(Float, default=0.0)
    release_date = Column(Date)


class Order(Base):
    __tablename__ = 'orders'

    id=Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))


