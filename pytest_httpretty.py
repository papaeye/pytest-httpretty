import functools

import httpretty


__version__ = '0.1.0'


def pytest_configure(config):
    config.addinivalue_line('markers',
                            'httpretty: mark tests to activate HTTPretty.')


def pytest_runtest_setup(item):
    marker = item.get_marker('httpretty')
    if marker is not None:
        httpretty.reset()
        httpretty.enable()


def pytest_runtest_teardown(item, nextitem):
    marker = item.get_marker('httpretty')
    if marker is not None:
        httpretty.disable()


stub_get = functools.partial(httpretty.register_uri, httpretty.GET)
