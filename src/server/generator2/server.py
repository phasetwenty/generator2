# Copyright 2017 Christopher Haverman
# All Rights Reserved
#
# Originally copied from https://docs.pylonsproject.org/projects/pyramid/en/stable/, which runs a hello world server.
#
from pyramid.config import Configurator
from pyramid.renderers import JSON

from .models import Instance

__author__ = 'Christopher Haverman'


def main(global_config, **settings):
    config = Configurator(settings=settings)
    config.add_route('home', '/')
    config.add_route('test', '/api/v1/test')
    config.add_route('instances', '/api/v1/properties/{property_id}/instances')
    config.add_route('random_object', '/api/v1/{slug}/random')
    config.include('.models')
    config.scan('.views')

    json_renderer = JSON()
    json_renderer.add_adapter(Instance, Instance.to_json)
    config.add_renderer('json', json_renderer)
    return config.make_wsgi_app()
