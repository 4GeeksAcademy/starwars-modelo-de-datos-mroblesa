from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import String, Boolean
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey, Integer
from typing import List


db = SQLAlchemy()

class User(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    email: Mapped[str] = mapped_column(String(120), unique=True, nullable=False)
    name: Mapped[str] = mapped_column(String(120), nullable=False)
    password: Mapped[str] = mapped_column(nullable=False)
    is_active: Mapped[bool] = mapped_column(Boolean(), nullable=False)



    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
            "name" : self.name
            # do not serialize the password, its a security breach
        }


class Planets(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(120), nullable=False)
    description: Mapped[str] = mapped_column(String(250), nullable= False)
    population: Mapped[int] = mapped_column(Integer, nullable=False)
    gravity: Mapped[int] = mapped_column(Integer, nullable=False)
    image: Mapped[str] = mapped_column(String(120), nullable=True)
    planets: Mapped[List["People"]] = relationship(back_populates='birth_planet')

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "description": self.description,
            "population": self.population,
            "gravity": self.gravity,
            "image": self.image,
            "planet_id": self.list
        }
    
class FavPlanet(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True, unique=True)
    planet_id : Mapped[int] = mapped_column(Integer, nullable= False)
    user_id: Mapped[int] = mapped_column(Integer, nullable=False)

    def serialize(self):
        return {
            "planet_id" : self.planet_id,
            "user_id" : self.user_id
        }

class People(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(120), nullable=False)
    age: Mapped[int] = mapped_column(Integer,nullable=False)
    gender: Mapped[str] = mapped_column(String(120), nullable=False)
    height: Mapped[str] = mapped_column(String(120), nullable=True)
    image: Mapped[str] = mapped_column(String(120), nullable=True)
    planet_id: Mapped[int] = mapped_column(Integer, ForeignKey("planets.id"))
    birth_planet: Mapped[str] = relationship(back_populates='planets')
    favorite: Mapped[List["FavPeople"]] = relationship(back_populates='fav_people_id')  # confirmar que he relacionado bien fav people 
    
    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "age": self.age,
            "gender": self.gender,
            "height": self.height,
            "image": self.image,
            "birth_planet": self.birth_planet
        }


class FavPeople(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True, unique=True)
    fav_people_id : Mapped[int] = mapped_column(Integer, ForeignKey("fav_people_id")) #confirmar relacion 
    user_id: Mapped[int] = mapped_column(Integer, nullable=False)


    def serialize(self):
        return {
            "people_id" : self.people_id,
            "user_id" : self.user_id
        }