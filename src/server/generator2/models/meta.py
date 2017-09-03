# Copyright 2017 Christopher Haverman
# All Rights Reserved
#
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.schema import MetaData

__author__ = 'Christopher Haverman'

NAMING_CONVENTION = {
    "ix": 'ix_%(column_0_label)s',
    "uq": "uq_%(table_name)s_%(column_0_name)s",
    "ck": "ck_%(table_name)s_%(constraint_name)s",
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
    "pk": "pk_%(table_name)s"
}
_metadata = MetaData(naming_convention=NAMING_CONVENTION)

Base = declarative_base(metadata=_metadata)
