# Copyright 2017 Christopher Haverman
# All Rights Reserved
#
# Originally copied from https://docs.pylonsproject.org/projects/pyramid/en/stable/, which runs a hello world server.
#
from pyramid.config import Configurator

__author__ = 'Christopher Haverman'


def main(global_config, **settings):
    config = Configurator(settings=settings)
    config.add_route('home', '/')
    config.add_route('test', '/api/v1/test')
    config.add_route('random_object', '/api/v1/random-object')
    config.include('.models')
    # config.include()
    config.scan('.views')
    return config.make_wsgi_app()
