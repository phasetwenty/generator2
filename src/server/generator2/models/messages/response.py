# Copyright 2017 Christopher Haverman
# All Rights Reserved
#
# Collection of messages that the API will respond with.
#
__author__ = 'Christopher Haverman'


class BaseMessage:
    """
    Defines the skeleton structure that the API messages have.

    Note that this was going to be inherited from ``dict`` as it acts like one, but the way the JSON codec is written it
    will try to serialized it like a dict and thus skip the custom functionality.
    """
    ERROR = 'error'
    OK = 'ok'

    def __init__(self, status, message):
        self.message = message
        self.status = status

    def __json__(self):
        return {'status': {'code': self.status, 'message': self.message}}


class DataMessage(BaseMessage):
    def __init__(self, message, data_key, data_value):
        super(DataMessage, self).__init__(self.OK, message)
        self._data_key = data_key
        if isinstance(data_value, (list, tuple)):
            self._data_value = data_value
        else:
            self._data_value = [data_value]

    def __json__(self):
        json = super(DataMessage, self).__json__()
        json[self._data_key] = self._data_value
        return json


class ErrorMessage(BaseMessage):
    def __init__(self, message):
        super(ErrorMessage, self).__init__(self.ERROR, message)


class InstanceMessage(DataMessage):
    def __init__(self, message, instances):
        super(InstanceMessage, self).__init__(message, 'instances', instances)


class ObjectMessage(DataMessage):
    def __init__(self, message, objects):
        super(ObjectMessage, self).__init__(message, 'objects', objects)
