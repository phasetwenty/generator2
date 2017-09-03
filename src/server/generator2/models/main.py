# Copyright 2017 Christopher Haverman
# All Rights Reserved
#
# Realized early that some aspects of table creation (e.g., using signed types for IDs) is not strictly optimal. I'm
# choosing to ignore that for now.
#
from sqlalchemy import Column, Integer, Text
from .meta import Base

__author__ = 'Christopher Haverman'


class Object(Base):
    __tablename__ = 'objects'
    id = Column(Integer, primary_key=True)
    name = Column(Text)
