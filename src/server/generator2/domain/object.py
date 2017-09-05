# Copyright 2017 Christopher Haverman
# All Rights Reserved
#
from random import randint
import logging

from sqlalchemy import text
from sqlalchemy.exc import DBAPIError

from ..models import Object

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

        random_object = {'name': my_object.name}
        try:
            for prop in my_object.properties:
                instance = prop.instances[randint(0, len(prop.instances) - 1)]
                random_object[prop.label] = instance.value
        except DBAPIError:
            _logger.exception('Failed to construct object')
            return None

        return random_object
