#!/bin/env python
import sys

sys.path.insert(0, '/var/www/api')

from app import create_app

application = create_app()
