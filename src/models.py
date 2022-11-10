import os
import sys

from eralchemy2 import render_er
from sqlalchemy import *
from sqlalchemy import create_engine
from sqlalchemy.dialects.postgresql import ARRAY
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import *

Base = declarative_base()

class Sections(Base):
    __tablename__ = 'sections'

    id = Column(Integer, primary_key=True)
    sections = Column(ARRAY(String(500)), nullable=False)


class Planets(Base):
    __tablename__ = 'planets'

    id = Column(Integer, primary_key=True)
    description = Column(String(250), nullable=True)
    diameter = Column(Integer, nullable=True)
    rotation_period = Column(Integer, nullable=True)
    orbital_period = Column(Integer, nullable=True)
    gravity = Column(String(250), nullable=True)
    population = Column(Integer, nullable=True)
    climate = Column(String(250), nullable=True)
    terrain = Column(String(250), nullable=True)
    surface_water = Column(Integer, nullable=True)
    name = Column(String(250), nullable=True)


class People(Base):
    __tablename__ = 'people'

    id = Column(Integer, primary_key=True)
    description = Column(String(250), nullable=True)
    height = Column(Integer, nullable=True)
    mass = Column(Integer, nullable=True)
    hair_color = Column(String(250), nullable=True)
    skin_color = Column(String(250), nullable=True)
    eye_color = Column(String(250), nullable=True)
    birth_year = Column(String(250), nullable=True)
    gender = Column(String(250), nullable=True)
    name = Column(String(250), nullable=True)
    homeworld = Column(Integer, ForeignKey('planets.id'))
    rels = relationship(Planets)


class Species(Base):
    __tablename__ = 'species'

    id = Column(Integer, primary_key=True)
    description = Column(String(250), nullable=True)
    classification = Column(String(250), nullable=True)
    designation = Column(String(250), nullable=True)
    average_height = Column(Integer, nullable=True)
    average_lifespan = Column(Integer, nullable=True)
    hair_colors = Column(String(250), nullable=True)
    skin_colors = Column(String(250), nullable=True)
    eye_colors = Column(String(250), nullable=True)
    language = Column(String(250), nullable=True)
    name = Column(String(250), nullable=True)
    # peoples es un array con las ids de people, no sé hasta que punto se puede relacionar esto
    peoples = Column(ARRAY(String(500)), ForeignKey('people.id'))
    homeworld = Column(Integer, ForeignKey('planets.id'))
    rels = relationship(Planets, People)


class Starships(Base):
    __tablename__ = 'starships'

    id = Column(Integer, primary_key=True)
    description = Column(String(250), nullable=True)
    model = Column(String(250), nullable=True)
    starship_class = Column(String(250), nullable=True)
    manufacturer = Column(String(250), nullable=True)
    cost_in_credits = Column(Integer, nullable=True)
    length = Column(Integer, nullable=True)
    crew = Column(String(250), nullable=True)
    passengers = Column(Integer, nullable=True)
    max_atmosphering_speed = Column(Integer, nullable=True)
    hyperdrive_rating = Column(String(250), nullable=True)
    MGLT = Column(Integer, nullable=True)
    cargo_capacity = Column(Integer, nullable=True)
    consumables = Column(String(250), nullable=True)
    pilots = Column(ARRAY(String(500)), ForeignKey('people.id'))
    name = Column(String(250), nullable=True)
    rels = relationship(People)


class Vehicles(Base):
    __tablename__ = 'vehicles'

    id = Column(Integer, primary_key=True)
    description = Column(String(250), nullable=True)
    model = Column(String(250), nullable=True)
    vehicle_class = Column(String(250), nullable=True)
    manufacturer = Column(String(250), nullable=True)
    cost_in_credits = Column(Integer, nullable=True)
    length = Column(Integer, nullable=True)
    crew = Column(String(250), nullable=True)
    passengers = Column(Integer, nullable=True)
    max_atmosphering_speed = Column(Integer, nullable=True)
    cargo_capacity = Column(Integer, nullable=True)
    consumables = Column(String(250), nullable=True)
    films = Column(ARRAY(String(500)), ForeignKey('films.id'))
    pilots = Column(ARRAY(String(500)), ForeignKey('people.id'))
    name = Column(String(250), nullable=True)
    rels = relationship(People, "Films")


class User(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    user = Column(String(250), nullable=False)
    password = Column(String(250), nullable=False)
    last_name = Column(String(250), nullable=True)
    email = Column(String(250), nullable=True)


class Films(Base):
    __tablename__ = 'films'

    id = Column(Integer, primary_key=True)
    description = Column(String(250), nullable=True)
    producer = Column(String(250), nullable=True)
    title = Column(String(250), nullable=True)
    episode_id = Column(String(250), nullable=True)
    director = Column(String(250), nullable=True)
    opening_crawl = Column(String(1250), nullable=True)
    # es people
    characters = Column(ARRAY(String(500)), ForeignKey('people.id'))
    planets = Column(ARRAY(String(500)), ForeignKey('planets.id'))
    starships = Column(ARRAY(String(500)), ForeignKey('starships.id'))
    vehicles = Column(ARRAY(String(500)), ForeignKey('vehicles.id'))
    species = Column(ARRAY(String(500)), ForeignKey('species.id'))
    rels = relationship(User, People, Planets, Starships, Vehicles, Species)


class Favorites(Base):
    __tablename__ = 'favorites'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    people = Column(ARRAY(String(500)), ForeignKey('people.id'))
    planets = Column(ARRAY(String(500)), ForeignKey('planets.id'))
    starships = Column(ARRAY(String(500)), ForeignKey('starships.id'))
    vehicles = Column(ARRAY(String(500)), ForeignKey('vehicles.id'))
    species = Column(ARRAY(String(500)), ForeignKey('species.id'))
    films = Column(ARRAY(String(500)), ForeignKey('films.id'))
    rels = relationship(User, People, Planets, Starships, Vehicles, Species, Films)

    def to_dict(self):
        return {}


# Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
