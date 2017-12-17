#!/usr/bin/python

# third party imports
from nose.tools import assert_is_not_none

# Local Imports

from project.services import get_todos

def test_request_response():
    # Call the service, which will send a request ot the server.
    response = get_todos()

    # if the request is sent succesfully, then exepect a response
    assert_is_not_none(response)


