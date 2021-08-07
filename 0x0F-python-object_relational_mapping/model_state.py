#!/usr/bin/python3
"""First state model."""

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    """ state class """
    __tablename__ = 'states'
    id = Column(Integer, nullable=False, autoincrement="auto",
                primary_key=True)
    name = Column(String(128), nullable=False)
