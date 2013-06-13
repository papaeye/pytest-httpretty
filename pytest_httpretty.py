import httpretty as _httpretty
import pytest


__version__ = '0.1.dev'


@pytest.fixture
def httpretty(request):
    _httpretty.httpretty.reset()
    _httpretty.httpretty.enable()
    request.addfinalizer(_httpretty.httpretty.disable)
    return _httpretty


@pytest.fixture
def stub_get(request, httpretty):
    def wrapper(*args, **kwargs):
        httpretty.register_uri(httpretty.GET, *args, **kwargs)
        return httpretty
    return wrapper
