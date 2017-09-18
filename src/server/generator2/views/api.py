# Copyright 2017 Christopher Haverman
# All Rights Reserved
#
from pyramid.response import Response
from pyramid.view import view_config

from ..domain.object import ObjectService
from .response import ApiResponse

__author__ = 'Christopher Haverman'


class Views:
    def __init__(self, request):
        self.request = request
        self.response = Response(content_type='application/json')
        self.response.headers['Access-Control-Allow-Origin'] = '*'

        self._object_service = ObjectService(request.dbsession)

    @view_config(route_name='test')
    def test(self):
        """
        Test endpoint used as a POC for getting data from the server.
        :return: Response
        """
        names = self._object_service.random_name()
        self.response.json = names
        return self.response

    @view_config(route_name='random_object')
    def random_object(self):
        slug = self.request.matchdict.get('slug', None)
        if not slug:
            self.response.status = 500
            self.response.text = 'Tried to get a random object but the slug was missing.'
            return self.response
        random_object = self._object_service.random_object(slug)
        if random_object is None:
            self.response.status = 500
            self.response.text = 'You got a bug homey'
        else:
            self.response.json = ApiResponse(objects=[random_object], status='ok').to_dict()
        return self.response
