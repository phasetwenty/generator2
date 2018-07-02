# Copyright 2018 Christopher Haverman
# All Rights Reserved
#
__author__ = 'Christopher Haverman'


class FormatMessage:
    """
    Describes the request to format an object.
    """
    def __init__(self, **kwargs):
        self.object = kwargs['object']
        self.format = kwargs['format']
        self.properties = kwargs['properties']


class FormatMessageValidator:
    """
    Validates the request to format an object. It might look like:
    {
        "object": "slug",
        "format": "format-string",
        "properties":
        {
            "name": "value"
        }
    }


    Perhaps replace with JSON schema? But then you have two problems.
    """
    def __init__(self):
        self.errors = None

    @property
    def is_valid(self):
        if self.errors is None:
            raise Exception('No message has been validated yet.')
        return len(self.errors) == 0

    def validate(self, **dict_message):
        self.errors = []
        self._validate_object(dict_message)
        self._validate_format(dict_message)
        self._validate_properties(dict_message)
        return self.errors

    def _validate_format(self, dict_message):
        format = dict_message.get('format')
        self._validate_string(format, 'format')

    def _validate_object(self, dict_message):
        object_ = dict_message.get('object')
        self._validate_string(object_, 'object')

    def _validate_properties(self, dict_message):
        properties = dict_message.get('properties')
        is_empty = self._verify_empty(properties, 'properties')
        if is_empty:
            return
        if len(properties) == 0:
            self.errors.append('"properties" must be nonempty.')

        wrong_type = self._verify_type(properties, dict, 'properties')
        if wrong_type:
            return

        bad_items = [v for _, v in properties.items() if not isinstance(v, str)]
        if len(bad_items) > 0:
            self.errors.append('Each member of "properties" must be a string.')

    def _validate_string(self, value, key_name):
        is_empty = self._verify_empty(value, key_name)
        if is_empty:
            return
        self._verify_type(value, str, key_name)

        if len(value) == 0:
            self.errors.append('"{}" must be a string of nonzero length.'.format(key_name))

    def _verify_empty(self, value, key_name):
        if value is None:
            self.errors.append('"{}" missing from request.'.format(key_name))
            return True
        return False

    def _verify_type(self, value, type_, key_name):
        if not isinstance(value, type_):
            type_value = type(value)
            self.errors.append('"{}" must be a nonempty string, but received {}.'.format(key_name, type_value.__name__))
            return True
        return False
