# Copyright 2017 Christopher Haverman
# All Rights Reserved
#
# getprops.py: script to drop the React initial props to stdout
#
from json import dumps

from pyramid.paster import get_appsettings, setup_logging
import transaction

from ..models import get_engine, get_session_factory, get_tm_session
from ..views.props import Props

__author__ = 'Christopher Haverman'


def main():
    config_uri = '/Users/Chris/Workspace/repos/generator2/src/server/dev.ini'
    setup_logging(config_uri)

    settings = get_appsettings(config_uri)
    engine = get_engine(settings)

    session_factory = get_session_factory(engine)
    with transaction.manager:
        dbsession = get_tm_session(session_factory, transaction.manager)
        props = Props(dbsession)
        print(dumps(props.to_dict()))

    return 0


if __name__ == '__main__':
    exit(main())
