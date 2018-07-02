# Copyright 2018 Christopher Haverman
# All Rights Reserved
#
from textwrap import dedent

__author__ = 'Christopher Haverman'


class PlainTextFormatter:
    """
    Takes a request to format some data and formats it in a plain-text format.
    """
    def __init__(self):
        pass

    def format(self, message):
        """
        :param message: FormatMessage instance to format.
        :return: str representation of the message.
        """
        properties = ['* {}: {}'.format(k, v) for k, v in message.properties.items()]
        return dedent(
            '''
            {}
        
            {}
            ''').format(message.object, '\n'.join(properties))
