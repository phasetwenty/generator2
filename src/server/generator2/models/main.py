# Copyright 2017 Christopher Haverman
# All Rights Reserved
#
# Realized early that some aspects of table creation (e.g., using signed types for IDs) is not strictly optimal. I'm
# choosing to ignore that for now.
#
# For more information on the concepts being modeled, see INTRO.md in the docs directory.
#
from sqlalchemy import Column, ForeignKey, Integer, Table, Text
from sqlalchemy.orm import relationship

from .meta import Base

__author__ = 'Christopher Haverman'


class Object(Base):
    __tablename__ = 'objects'
    id = Column(Integer, primary_key=True)
    name = Column(Text)

    properties = relationship('Property', back_populates='object')

    def __str__(self):
        return self.name


property_tag_lookup_table = Table(
    'property_tags',
    Base.metadata,
    Column('property_id', Integer, ForeignKey('properties.id')),
    Column('tag_id', Integer, ForeignKey('tags.id'))
)


class Property(Base):
    __tablename__ = 'properties'
    id = Column(Integer, primary_key=True)
    label = Column(Text)
    object_id = Column(Integer, ForeignKey('objects.id'))

    instances = relationship('Instance', back_populates='property')
    object = relationship('Object', back_populates='properties')
    tags = relationship('Tag', secondary=property_tag_lookup_table, back_populates='properties')

    def __str__(self):
        return self.label


class Instance(Base):
    __tablename__ = 'instances'
    id = Column(Integer, primary_key=True)
    value = Column(Text)
    property_id = Column(Integer, ForeignKey('properties.id'))

    property = relationship('Property', back_populates='instances')

    def __str__(self):
        return self.value


class Tag(Base):
    __tablename__ = 'tags'
    id = Column(Integer, primary_key=True)
    name = Column(Text)

    properties = relationship('Property', secondary=property_tag_lookup_table, back_populates='tags')

    def __str__(self):
        return self.name
