# Copyright 2016 Christopher Haverman
# All Rights Reserved
#
from unittest.mock import Mock, PropertyMock
import pytest

from sqlalchemy.orm.session import Session

from generator2.domain.object import ObjectService


class TestObjectService:
    def test_full_object(self, dbsession, object_):
        """
        Ensures that the shape of the dict returned matches expectations.

        The object being tested for looks like:
        {
            "kind": "bovine",
            "slug": "cowslug",
            "properties": [
                {
                    "label": "The cow says",
                    "instances": ["moo"]
                },
                {
                    "label": "name",
                    "instances": ["aloysius"]
                }
            ]
        }
        """
        object_under_test = ObjectService(dbsession)
        actual_object = object_under_test.full_object('cowslug')
        assert 'bovine' == actual_object.get('kind')
        assert 'cowslug' == actual_object.get('slug')
        assert 2 == len(actual_object['properties'])

        property_ = actual_object.get('properties')[0]
        assert 'The cow says' == property_.get('label')
        assert 1 == len(property_.get('instances'))

        name = actual_object.get('properties')[1]
        assert 'name' == name.get('label')
        assert ['aloysius'] == name.get('instances')

        instance = property_.get('instances')[0]
        assert 'moo' == instance

    @pytest.fixture
    def dbsession(self, object_, additional_properties):
        dbsession = Mock(Session)
        _lookup_object = Mock()
        _lookup_object.filter.return_value.one.return_value = object_
        _object_additional_properties = Mock()
        _object_additional_properties.filter.return_value.all.return_value = additional_properties
        dbsession.query.side_effect = (_lookup_object, _object_additional_properties)
        return dbsession

    @pytest.fixture
    def instance(self):
        instance = Mock()
        type(instance).value = PropertyMock(return_value='moo')
        return instance

    @pytest.fixture
    def additional_instance(self):
        instance = Mock()
        type(instance).value = PropertyMock(return_value='aloysius')
        return instance

    @pytest.fixture
    def object_(self, property_):
        object_ = Mock()
        type(object_).kind = PropertyMock(return_value='bovine')
        type(object_).slug = PropertyMock(return_value='cowslug')
        type(object_).properties = PropertyMock(return_value=[property_])
        return object_

    @pytest.fixture
    def property_(self, instance):
        property_ = Mock()
        type(property_).label = PropertyMock(return_value='The cow says')
        type(property_).instances = PropertyMock(return_value=[instance])
        return property_

    @pytest.fixture
    def additional_properties(self, additional_instance):
        property_ = Mock()
        type(property_).label = PropertyMock(return_value='name')
        type(property_).instances = PropertyMock(return_value=[additional_instance])
        return [property_]
