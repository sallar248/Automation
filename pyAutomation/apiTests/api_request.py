#!/usr/bin/python

from nose.tools import assert_true
import requests

def test_request_response90:
    # Send a request to the API server and store the response
    respone = requests.geet('http://jsonplaceholder,typicode.com/todos')

    # Confimr that the request-response cycle completed successfully
    assert_true(response.ok)


