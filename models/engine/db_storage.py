#!/usr/bin/python3
"""
Module for our new MySQL Storage
"""
import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from models.base_model import Base
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review

classes = {
    "User": User,
    "State": State,
    "City": City,
    "Amenity": Amenity,
    "Place": Place,
    "Review": Review
    }


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
        env = os.environ.get("HBNB_ENV")

        # print(user, password, host, database, env)

        self.__engine = create_engine("mysql+mysqldb://{}:{}@{}/{}".format(
                            user, password, host, database),
                            pool_pre_ping=True
                        )

        Session = sessionmaker(bind=self.__engine)
        self.__session = Session()

        if env == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """Query all the objects depending on the class name (cls)"""

        objects = {}
        if cls:
            class_name = eval(cls).__name__
            result = self.__session.query(classes[class_name]).all()
            for obj in result:
                key = f"{cls}.{obj.id}"
                objects[key] = obj
        else:
            for class_ in classes:
                result = self.__session.query(class_).all()
                for obj in result:
                    key = f"{class_}.{obj.id}"
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
        Session = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Base.metadata.create_all(self.__engine)
        # Use scoped_session to ensure thread safety
        self.__session = scoped_session(Session)

    def close(self):
        """Calls remove() method on the private session attribute"""
        self.__session.close()
