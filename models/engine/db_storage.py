#!/usr/bin/python3
"""
Module for our new MySQL Storage
"""
import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from models.base_model import Base


class DBStorage:
    """Class file for the Database Storage"""

    __engine = None
    __session = None

    def __init__(self):
        """
        Creates the Engine and sets it's parameters appropriately
        """
        user = os.environ.get("HBNB_MYSQL_USER")
        password = os.environ.get("HBNB_MYSQL_PWD")
        host = os.environ.get("HBNB_MYSQL_HOST")
        database = os.environ.get("HBNB_MYSQL_DB")

        self.__engine = create_engine("mysql+mysqldb://{}:{}@{}/{}".format(
                            user, password, host, database),
                            pool_pre_ping=True
                        )

        Session = sessionmaker(bind=self.__engine)
        self.__session = Session()

        if os.environ.get("HBNB_ENV") == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """Query all the objects depending on the class name (cls)"""
        from models import User, State, City, Amenity, Place, Review

        if cls is None:
            classes = [User, State, City, Amenity, Place, Review]
        else:
            classes = [cls]

        objects = {}

        for class_ in classes:
            class_name = class_.__name__
            result = self.__session.query(class_).all()

            for obj in result:
                key = f"{class_name}.{obj.id}"
                objects[key] = obj

        return objects

    def new(self, obj):
        """Adds the object to the current database session"""
        self.__session.add(obj)

    def save(self):
        """Commits all changes of the current database session"""
        self.__session.commit()

    def delete(self, obj=None):
        """Delete from the current database session obj if not None"""
        if obj:
            self.__session.delete(obj)

    def reload(self):
        """Reloads all tables in the database and creates a new session"""

        # Create all tables in the database
        Base.metadata.create_all(self.__engine)

        # Create a new session with sessionmaker and bind it to the engine
        Session = sessionmaker(bind=self.__engine, expire_on_commit=False)

        # Use scoped_session to ensure thread safety
        self.__session = scoped_session(Session)

    def close(self):
        """Calls remove() method on the private session attribute"""
        self.__session.close()