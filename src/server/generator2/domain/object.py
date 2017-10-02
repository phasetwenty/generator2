# Copyright 2017 Christopher Haverman
# All Rights Reserved
#
from random import randint
import logging

from sqlalchemy.exc import DBAPIError
from sqlalchemy.orm.exc import NoResultFound

from .exceptions import DatabaseLookupFailedError
from ..models import Object, Property

__author__ = 'Christopher Haverman'

_logger = logging.getLogger(__name__)


class ObjectService:
    """
    First pass at a service for creating random objects.
    """
    def __init__(self, dbsession):
        self._dbsession = dbsession

    def random_object(self, slug):
        """
        :param slug: DB slug to match an object to.
        :return: A dict mapping property labels to instances. If the slug did not match an entry, None is returned.
        :raise DatabaseLookupFailedError: When the underlying database operations fail.
        """
        try:
            my_object = self._dbsession.query(Object).filter(Object.slug == slug).one()
        except NoResultFound:
            return None
        except DBAPIError as e:
            raise DatabaseLookupFailedError('Unable to look up object with slug "{}".'.format(slug)) from e

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
