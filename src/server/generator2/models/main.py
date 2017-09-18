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


class Category(Base):
    __tablename__ = 'categories'
    id = Column(Integer, primary_key=True)
    name = Column(Text, nullable=False)

    subcategories = relationship('Subcategory', back_populates='category')
    objects = relationship('Object', back_populates='category')
    properties = relationship('Property', back_populates='category')

    def __str__(self):
        return self.name


class Subcategory(Base):
    __tablename__ = 'subcategories'
    id = Column(Integer, primary_key=True)
    name = Column(Text, nullable=False)
    category_id = Column(Integer, ForeignKey('categories.id'), nullable=False)

    category = relationship('Category', back_populates='subcategories')
    objects = relationship('Object', back_populates='subcategory')
    properties = relationship('Property', back_populates='subcategory')

    def __str__(self):
        return self.name


class Object(Base):
    __tablename__ = 'objects'
    id = Column(Integer, primary_key=True)
    kind = Column(Text, nullable=False)
    slug = Column(Text, nullable=False)
    category_id = Column(Integer, ForeignKey('categories.id'), nullable=False)
    subcategory_id = Column(Integer, ForeignKey('subcategories.id'))

    category = relationship('Category', back_populates='objects')
    properties = relationship('Property', back_populates='object')
    subcategory = relationship('Subcategory', back_populates='objects')

    def __str__(self):
        return self.kind


class Property(Base):
    __tablename__ = 'properties'
    id = Column(Integer, primary_key=True)
    label = Column(Text, nullable=False)
    category_id = Column(Integer, ForeignKey('categories.id'), nullable=False)
    subcategory_id = Column(Integer, ForeignKey('subcategories.id'))
    object_id = Column(Integer, ForeignKey('objects.id'))

    category = relationship('Category', back_populates='properties')
    instances = relationship('Instance', back_populates='property')
    subcategory = relationship('Subcategory', back_populates='properties')
    object = relationship('Object', back_populates='properties')

    def __str__(self):
        return self.label


class Instance(Base):
    __tablename__ = 'instances'
    id = Column(Integer, primary_key=True)
    value = Column(Text)
    property_id = Column(Integer, ForeignKey('properties.id'), nullable=False)

    property = relationship('Property', back_populates='instances')

    def __str__(self):
        return self.value
