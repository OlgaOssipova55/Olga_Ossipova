
'''
# Python-скрипт для подключения к БД SQL
from sqlalchemy import create_engine, Column, Integer, String, Sequence
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class Person(Base):
    __tablename__ = 'user'
    id = Column (Integer, Sequence('user_id_seq'), primary_key=True)
    name = Column (String(50))
    age = Column (Integer)

# Расширение скрипта с использованием try/except
try:
    engine = create_engine ('sqlite:///:memory:', echo=True)
    Base.metadata.create_all(bind=engine)
    Session = sessionmaker (bind=engine)
    session = Session ()
    
    person1 = Person (name = 'Olga      ', age = 20)
    person2 = Person (name = 'Oleg', age = 30)

    session.add_all ([person1, person2])
    session.commit()
    
    people = session.query(Person).all()
    for person in people:
        print (f"ID: {person.id}, имя: {person.name}, возраст: {person.age}")

except Exception as e:
    print(f"Error: {e}")

finally:
    session.close()
    engine.dispose()
'''

# Скрипт, использующий ORM
from sqlalchemy import create_engine, Column, Integer, String, Sequence
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import SQLAlchemyError

Base = declarative_base()

class Person(Base):
    __tablename__ = 'user'
    id = Column(Integer, Sequence('user_id_seq'), primary_key=True)
    name = Column(String(50))
    age = Column(Integer)


engine = create_engine('sqlite:///:memory:', echo=True)
Base.metadata.create_all(bind=engine)
Session = sessionmaker(bind=engine)
session = Session()

session.begin_nested()

try:
    person3 = Person(name='Grigoriy', age=22)
    session.add(person3)

    duplicate_user = Person(name='Grigoriy', age=22)
    session.add(duplicate_user)

    session.commit()

except SQLAlchemyError as e:
    print(f"SQLAlchemyError: {e}")
    session.rollback()

finally:
    session.close()
    engine.dispose()
