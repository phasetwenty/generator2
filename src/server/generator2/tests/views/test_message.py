# Copyright 2016 Christopher Haverman
# All Rights Reserved
#
import pytest

from generator2.views.message import BaseMessage, DataMessage


class TestBaseMessage:
    def test_json(self):
        """
        Ensures the serialization protocol has the required schema.
        """
        expected_json = {'status': {'code': 'horse', 'message': 'a different horse'}}
        actual_json = BaseMessage('horse', 'a different horse').__json__()
        assert expected_json == actual_json


class TestDataMessage:
    json_cases = (
        (
            {'status': {'code': 'ok', 'message': 'fakemessage'}, 'datakey': ['datavalue']},
            DataMessage('fakemessage', 'datakey', ['datavalue'])
        ),
        (
            {'status': {'code': 'ok', 'message': 'fakemessage'}, 'datakey': ['datavalue']},
            DataMessage('fakemessage', 'datakey', 'datavalue')
        ),
    )

    @pytest.mark.parametrize('expected_json,object_under_test', json_cases)
    def test_json(self, expected_json, object_under_test):
        """
        Given that we expect all data messages to be given as a collection, this test ensures that if it receives a
        singleton value that it gets put into a list.
        """
        assert expected_json == object_under_test.__json__()
