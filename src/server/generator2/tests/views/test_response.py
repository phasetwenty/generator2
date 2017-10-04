# Copyright 2016 Christopher Haverman
# All Rights Reserved
#
import pytest

from generator2.views.response import ApiJsonEncoder


class ConformingClass:
    """
    Class used as a fixture for ``TestApiJsonEncoder``.
    """

    def __json__(self):
        return {'oh': 'hi'}


class NonconformingClass:
    """
    Class used as a fixture for ``TestApiJsonEncoder``.
    """


class TestApiJsonEncoder:
    def test_default(self):
        """
        Ensures that when the encoder sees a type it doesn't natively understand, that it invokes the __json__ protocol
        to serialize the type.
        """
        object_under_test = ApiJsonEncoder()
        actual_json = object_under_test.encode(ConformingClass())
        assert '{"oh": "hi"}' == actual_json

    def test_default_raises(self):
        """
        Ensures that when the encoder sees a type that it doesn't natively understand and does not implement the
        __json__ protocol, it raises the expected exception.
        """
        object_under_test = ApiJsonEncoder()
        with pytest.raises(TypeError):
            object_under_test.encode(NonconformingClass())
