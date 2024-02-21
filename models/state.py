#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey
from models import storage, storage_type


class State(BaseModel, Base):
    """ State class to add a new state object"""
    if storage_type == "db":
        
        __tablename__ = 'states'

        name = Column(String(128), nullable=False)
        cities = relationship("City", backref="state",
                            cascade="all, delete-orphan")
    else:
        name = ""
        self.__super().__init__(*args, **kwargs)
