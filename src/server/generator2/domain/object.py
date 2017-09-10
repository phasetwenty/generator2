# Copyright 2017 Christopher Haverman
# All Rights Reserved
#
from random import randint
import logging

from sqlalchemy import or_
from sqlalchemy.exc import DBAPIError

from ..models import Instance, Object, Property

__author__ = 'Christopher Haverman'

_logger = logging.getLogger(__name__)


class ObjectService:
    """
    First pass at a service for creating random objects.
    """
    def __init__(self, dbsession):
        self._dbsession = dbsession

    @property
    def random_object(self):
        try:
            my_object = self._dbsession.query(Object).first()
        except DBAPIError:
            _logger.exception('Failed to lookup object in database')
            return None

        additional_properties = (self._dbsession.query(Property).filter(
            Property.category == my_object.category,
            Property.subcategory == my_object.subcategory,
            Property.object_id == None)).all()
        properties = my_object.properties + additional_properties
        random_object = {
            property.label: property.instances[randint(0, len(property.instances) - 1)].value
            for property in properties
        }
        return random_object
