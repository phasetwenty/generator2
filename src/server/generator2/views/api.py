# Copyright 2017 Christopher Haverman
# All Rights Reserved
#
from json import JSONDecodeError
import logging

from pyramid.view import view_config

from ..domain import DatabaseLookupFailedError, ObjectService, PropertyService
from ..domain.formatters import PlainTextFormatter
from ..models.messages.response import ErrorMessage, InstanceMessage, ObjectMessage
from ..models.messages.request import FormatMessage, FormatMessageValidator
from .request import ApiJsonDecoder
from .response import ApiJsonEncoder, ApiResponse

__author__ = 'Christopher Haverman'

_logger = logging.getLogger(__name__)


class Views:
    def __init__(self, request):
        self.request = request
        self.response = ApiResponse(ApiJsonEncoder(), content_type='application/json')
        self.response.headers['Access-Control-Allow-Origin'] = '*'

        self._object_service = ObjectService(request.dbsession)
        self._property_service = PropertyService(request.dbsession)
        self._request_decoder = ApiJsonDecoder()
        self._formatter = PlainTextFormatter()
        self._format_message_validator = FormatMessageValidator()

    @view_config(route_name='format')
    def format(self):
        body = None
        # noinspection PyBroadException
        try:
            str_body = self.request.body.decode('utf-8')
            body = self._request_decoder.decode(str_body)
        except JSONDecodeError:
            _logger.exception('Error parsing json')
            self.response.status_code = 400
            self.response.json = {'error': 'invalid json homey'}
            return self.response
        except Exception:
            _logger.exception('Unhandled exception while decoding format request.')
            self.response.status_code = 500
            self.response.json = {'error': 'invalid json homey'}
            return self.response

        self._format_message_validator.validate(**body)
        if not self._format_message_validator.is_valid:
            self.response.status_code = 400
            self.response.json = {'error': ' '.join(self._format_message_validator.errors)}
            return self.response

        message = FormatMessage(**body)

        self.response.text = self._formatter.format(message)
        return self.response

    @view_config(route_name='instances')
    def instances(self):
        property_id = self.request.matchdict.get('property_id')
        try:
            instances = self._property_service.instances_for_id(property_id)
        except DatabaseLookupFailedError:
            _logger.exception('Database lookup failed.')
            self.response.status_code = 500
            message = 'There was a problem fetching instances for property ID {}'.format(property_id)
            self.response.json = ErrorMessage(message)
        else:
            self.response.json = InstanceMessage('', instances)
        return self.response

    @view_config(route_name='object')
    def object(self):
        return self._object_helper(self._object_service.full_object)

    @view_config(route_name='random_object')
    def random_object(self):
        return self._object_helper(self._object_service.random_object)

    def _object_helper(self, lookup_fn):
        slug = self.request.matchdict.get('slug', None)
        if not slug:
            self.response.status_code = 400
            self.response.json = ErrorMessage('Tried to lookup an object but the slug was missing.')
            return self.response
        try:
            random_object = lookup_fn(slug)
        except DatabaseLookupFailedError:
            _logger.exception('Database lookup failed.')
            self.response.status = 500
            self.response.json = ErrorMessage('Unknown failure looking up object with slug "{}".'.format(slug))
        else:
            if random_object is None:
                self.response.status = 404
                self.response.json = ErrorMessage('No object named "{}" found.'.format(slug))
                return self.response
            self.response.json = ObjectMessage('', [random_object])
        return self.response
