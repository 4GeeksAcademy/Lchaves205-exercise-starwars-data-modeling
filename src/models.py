import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class People(Base):
    __tablename__ = 'people'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    height = Column(String(250))
    gender = Column(String(250))


class Planet(Base):
    __tablename__ = 'planet'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    population = Column(String(250))
    diameter = Column(String(250))

class Vehicle(Base):
    __tablename__ = 'vehicle'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    cargo_capacity = Column(String(250))
    consumables = Column(String(250))


class Starship(Base):
    __tablename__ = 'starship'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    cargo_capacity = Column(String(250))
    consumables = Column(String(250))


class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    email = Column(String(250), nullable=False)
    address = Column(String(250))

class Favorites(Base):
    __tablename__ = 'favorites'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    planet_id = Column(Integer, ForeignKey('planet.id'), nullable=True)
    people_id = Column(Integer, ForeignKey('people.id'), nullable=True)
    starship_id = Column(Integer, ForeignKey('starship.id'), nullable=True)
    vehicle_id = Column(Integer, ForeignKey('vehicle.id'), nullable=True)

    user = relationship(User)
    planet = relationship(Planet)
    people = relationship(People)
    starship = relationship(Starship)
    vehicle = relationship(Vehicle)


## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
