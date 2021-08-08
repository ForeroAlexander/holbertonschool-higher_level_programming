#!/usr/bin/python3
""" contains the class definition of a City. """

from sys import argv
from model_state import Base, State
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base


class City(Base):
    """
    create table
    """
    __tablename__ = "cities"
    id = Column("id", Integer(), autoincrement=True,
                nullable=False, primary_key=True)
    name = Column("name", String(128), nullable=False)
    state_id = Column(Integer(), ForeignKey("states.id"), nullable=False)
