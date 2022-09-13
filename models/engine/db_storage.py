#!/usr/bin/python3
"""This module defines a class User"""
from models.base_model import BaseModel, Base
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy.ext.declarative import declarative_base
import os
from sqlalchemy import create_engine
from models.state import State
from models.city import City
from models.place import Place
from models.review import Review
from models.amenity import Amenity
from models.user import User


alvclasses = {"State": State, "City": City, "User": User, "Place": Place,
              "Review": Review, "Amenity": Amenity}


class DBStorage:
    '''Class db storage'''
    __engine = None
    __session = None

    def __init__(self):
        '''Constructor'''
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'
                                      .format(os.getenv('HBNB_MYSQL_USER'),
                                              os.getenv('HBNB_MYSQL_PWD'),
                                              os.getenv('HBNB_MYSQL_HOST'),
                                              os.getenv('HBNB_MYSQL_DB')),
                                      pool_pre_ping=True)
        if os.getenv('HBNB_ENV') == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """Query on the current database session"""
        newdict = {}
        for clase in alvclasses:
            if cls is None:
                obj = self.__session.query(alvclasses[clase]).all()
                for instance in obj:
                    key = instance.__class__.__name__ + '.' + instance.id
                    newdict[key] = instance
            elif cls:
                obj = self.__session.query(alvclasses[cls]).all()
                for instance in obj:
                    key = instance.__class__.__name__ + '.' + instance.id
                    newdict[key] = instance
        return newdict

    def new(self, obj):
        '''Adds new object to storage dictionary'''
        self.__session.add(obj)

    def save(self):
        '''Saves storage dictionary to file'''
        self.__session.commit()

    def delete(self, obj=None):
        '''delete obj from __objects if it’s inside'''
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        '''Loads storage dictionary from file'''
        Base.metadata.create_all(self.__engine)
        sess = sessionmaker(bind=self.__engine, expire_on_commit=False)
        self.__session = scoped_session(sess)
