# Copyright 2017 Christopher Haverman
# All Rights Reserved
#
from pyramid.response import Response
from pyramid.view import view_config
from sqlalchemy.exc import DBAPIError

from ..models.main import Object

__author__ = 'Christopher Haverman'


class Views:
    def __init__(self, request):
        self.request = request
        self.response = Response(content_type='application/json')
        self.response.headers['Access-Control-Allow-Origin'] = '*'

    @view_config(route_name='test')
    def test(self):
        """
        Test endpoint used as a POC for getting data from the server.
        :return: Response
        """
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

    @view_config(route_name='dbfetch')
    def dbfetch(self):
        try:
            query = self.request.dbsession.query(Object)
            test_obj = query.first()
        except DBAPIError:
            self.response.status = 500
            return self.response

        self.response.json = {'object': test_obj.name}
        return self.response
