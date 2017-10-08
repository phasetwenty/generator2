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

    def full_object(self, slug):
        """
        :param slug: DB slug to match an object to. If the slug did not match an entry, None is returned.
        :return: A dict describing the object along with additional nested members for its properties and each
        property's instances.
        :raise DatabaseLookupFailedError: When the underlying database operations fail.
        """
        my_object = self._lookup_object(slug)
        additional_properties = self._object_additional_properties(my_object)
        properties = my_object.properties + additional_properties
        return {
            "kind": my_object.kind,
            "slug": my_object.slug,
            "properties": [
                {
                    "label": property_.label,
                    "instances": [instance.value for instance in property_.instances]
                }
                for property_ in properties
            ]
        }

    def random_object(self, slug):
        """
        :param slug: DB slug to match an object to.
        :return: A dict mapping property labels to instances. If the slug did not match an entry, None is returned.
        :raise DatabaseLookupFailedError: When the underlying database operations fail.
        """
        my_object = self._lookup_object(slug)
        additional_properties = self._object_additional_properties(my_object)

        properties = my_object.properties + additional_properties
        random_object = {
            property.label: property.instances[randint(0, len(property.instances) - 1)].value
            for property in properties
        }
        return random_object

    def _object_additional_properties(self, object_):
        return (self._dbsession.query(Property).filter(
            Property.category == object_.category,
            Property.subcategory == object_.subcategory,
            Property.object_id == None)).all()

    def _lookup_object(self, slug):
        try:
            return self._dbsession.query(Object).filter(Object.slug == slug).one()
        except NoResultFound:
            return None
        except DBAPIError as e:
            raise DatabaseLookupFailedError('Unable to look up object with slug "{}".'.format(slug)) from e
