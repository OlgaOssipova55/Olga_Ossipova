from sqlalchemy import create_engine, Column, Integer, String, Sequence
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class Person(Base):
    __tablename__ = 'user'
    id = Column (Integer, Sequence('user_id_seq'), primary_key=True)
    name = Column (String(50))
    age = Column (Integer)


engine = create_engine ('sqlite:///:memory:', echo=True)
Base.metadata.create_all(bind=engine)
Session = sessionmaker (bind=engine)
session = Session ()

person1 = Person (name = 'Olga', age = 20)
person2 = Person (name = 'Oleg', age = 30)

session.add_all ([person1, person2])
session.commit()

people = session.query(Person).all()
for person in people:
    print (f"ID: {person.id}, имя: {person.name}, возраст: {person.age}")
