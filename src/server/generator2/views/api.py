# Copyright 2017 Christopher Haverman
# All Rights Reserved
#
from pyramid.response import Response
from pyramid.view import view_config

import logging

__author__ = 'Christopher Haverman'

_logger = logging.getLogger(__name__)


class Views:
    def __init__(self, request):
        self.request = request
        self.response = Response(content_type='application/json')
        self.response.headers['Access-Control-Allow-Origin'] = '*'

    @view_config(route_name='test')
    def test(self):
        self.response.json = [
            ('Name', 'Horse'),
            ('Sex', 'Male'),
            ('Race', 'Human'),
            ('Class', 'Horse'),
            (
                'Description',
                'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Fusce faucibus nunc massa, et tempus tortor '
                'rhoncus eget. Aenean volutpat.'
            ),
            ('Extra', 'Lorem ipsum dolor sit amet, consectetur adipiscing metus.')
        ]
        return self.response
