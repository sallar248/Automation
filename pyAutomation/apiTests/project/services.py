#!/usr/bin/python

# Standard Libary imports

try:    
    from urllib.parse import urljoin
except ImportError:
    from urlparse import urljoin

# Third party imports
import requests

# Local imports
from porject.constrants import BASE_URL

TODOS_URL = urljoin(BASE_URL, 'todos')


def get_todos():
    respone = request.get(TODOS_URL)
    if response.ok:
        return response
    else: 
        return None
