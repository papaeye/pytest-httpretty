import requests


def test_httpretty(httpretty):
    httpretty.register_uri(httpretty.GET, 'http://example.com/', body='Hello')

    assert requests.get('http://example.com').text == 'Hello'


def test_stub_get(stub_get):
    stub_get('http://example.com/', body='World!')

    assert requests.get('http://example.com').text == 'World!'
