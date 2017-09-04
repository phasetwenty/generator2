# Copyright 2017 Christopher Haverman
# All Rights Reserved
#
import os
import sys

try:
    from pyramid.paster import get_appsettings, setup_logging
    from pyramid.scripts.common import parse_vars
except ImportError:
    sys.stderr.write('Pyramid is missing from this environment. Perhaps you need to activate your virtualenv?')
    sys.exit(1)

from generator2.models import get_engine
from generator2.models.meta import Base

__author__ = 'Christopher Haverman'


def usage(argv):
    cmd = os.path.basename(argv[0])
    print('usage: %s <config_uri> [var=value]\n'
          '(example: "%s development.ini")' % (cmd, cmd))
    sys.exit(1)


def main(argv=None):
    argv = argv or sys.argv
    if len(argv) < 2:
        usage(argv)
    config_uri = argv[1]
    options = parse_vars(argv[2:])
    setup_logging(config_uri)
    settings = get_appsettings(config_uri, options=options)

    engine = get_engine(settings)
    Base.metadata.create_all(engine)
