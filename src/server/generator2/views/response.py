# Copyright 2017 Christopher Haverman
# All Rights Reserved
#
from json import JSONEncoder

from pyramid.response import Response

__author__ = 'Christopher Haverman'


class ApiJsonEncoder(JSONEncoder):
    """
    Encoder customized to add a serialization protocol to custom objects.
    """

    def default(self, o):
        try:
            return o.__json__()
        except AttributeError:
            message = ("Object of type '{}' is not JSON serializable "
                       "and does not implement the custom protocol.").format(o.__class__.__name__)
            raise TypeError(message)


class ApiResponse(Response):
    """
    Response class that implements the custom JSON encoding.
    """

    def __init__(self, encoder, **kwargs):
        super(ApiResponse, self).__init__(**kwargs)
        self._encoder = encoder

    def _set_json(self, value):
        # The additional call to str.encode() is needed because the superclass' body member expects this to be given as
        # an iterable of bytes instead of a string.
        #
        # noinspection PyAttributeOutsideInit
        self.body = self._encoder.encode(value).encode('UTF-8')

    # noinspection PyProtectedMember
    json = property(Response._json_body__get, _set_json, Response._json_body__del)
