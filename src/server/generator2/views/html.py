# Copyright 2017 Christopher Haverman
# All Rights Reserved
#
from pyramid.view import view_config, view_defaults

__author__ = 'Christopher Haverman'


@view_defaults(renderer='generator2:templates/home.jinja2')
class Views:
    def __init__(self, request):
        self.request = request

    @view_config(route_name='home')
    def home(self):
        return {}
