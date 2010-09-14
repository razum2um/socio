#!/usr/bin/env python
from django.core.management import execute_manager
import os
import sys


def rel(*x):
    return os.path.join(os.path.abspath(os.path.dirname(__file__)), *x)


paths = ('apps','contrib')

for path in paths:
    path = rel(path)
    if path not in sys.path:
        sys.path.append(path)



try:
    import settings # Assumed to be in the same directory.
except ImportError:
    import sys
    sys.stderr.write("Error: Can't find the file 'settings.py' in the directory containing %r. It appears you've customized things.\nYou'll have to run django-admin.py, passing it your settings module.\n(If the file settings.py does indeed exist, it's causing an ImportError somehow.)\n" % __file__)
    sys.exit(1)

if __name__ == "__main__":
    execute_manager(settings)

