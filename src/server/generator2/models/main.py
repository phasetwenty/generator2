# Copyright 2017 Christopher Haverman
# All Rights Reserved
#
# Realized early that some aspects of table creation (e.g., using signed types for IDs) is not strictly optimal. I'm
# choosing to ignore that for now.
#
# For more information on the concepts being modeled, see INTRO.md in the docs directory.
#
from sqlalchemy import Column, ForeignKey, Integer, Text
from sqlalchemy.orm import relationship

from .meta import Base

__author__ = 'Christopher Haverman'


class Object(Base):
    __tablename__ = 'objects'
    id = Column(Integer, primary_key=True)
    name = Column(Text)

    properties = relationship('Property', back_populates='object')


class Property(Base):
    __tablename__ = 'properties'
    id = Column(Integer, primary_key=True)
    descriptor = Column(Text)
    object_id = Column(Integer, ForeignKey('objects.id'))

    instances = relationship('Instance', back_populates='property')
    object = relationship('Object', back_populates='properties')


class Instance(Base):
    __tablename__ = 'instances'
    id = Column(Integer, primary_key=True)
    value = Column(Text)
    property_id = Column(Integer, ForeignKey('properties.id'))

    property = relationship('Property', back_populates='instances')
