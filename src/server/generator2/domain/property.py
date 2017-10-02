# Copyright 2017 Christopher Haverman
# All Rights Reserved
#
import logging

from sqlalchemy.exc import DBAPIError
from sqlalchemy.orm.exc import NoResultFound

from .exceptions import DatabaseLookupFailedError
from ..models import Property

__author__ = 'Christopher Haverman'

_logger = logging.getLogger(__name__)


class PropertyService:
    """
    Service for obtaining data relating to properties.
    """
    def __init__(self, dbsession):
        self._dbsession = dbsession

    def instances_for_id(self, property_id):
        try:
            return self._dbsession.query(Property).filter(Property.id == property_id).one().instances
        except NoResultFound:
            return []
        except DBAPIError as e:
            raise DatabaseLookupFailedError('Database lookup failed for property ID {}.'.format(property_id)) from e
