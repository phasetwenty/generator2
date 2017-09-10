# Copyright 2017 Christopher Haverman
# All Rights Reserved
#
__author__ = 'Christopher Haverman'


class ApiResponse:
    """
    Value object designed to formalize this API's response schema.
    """
    ERROR = 'error'
    OK = 'ok'

    def __init__(self, **kwargs):
        """
        :keyword message: A UI-facing error message, or empty.
        :keyword objects: Iterable of objects (in the domain sense).
        :keyword status: Either "error" (default) or "ok".
        """
        self.message = kwargs.get('message', '')
        self.objects = kwargs.get('objects', [])
        self.status = kwargs.get('status', self.ERROR)

    def to_dict(self):
        return {
            'status': {
                'code': self.status,
                'message': self.message
            },
            'objects': self.objects
        }
