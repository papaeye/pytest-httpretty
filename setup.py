import os.path
import re

from setuptools import setup


def read(filename):
    path = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                        filename)
    return open(path).read()


__version__ = re.search("^__version__ = '(.+)'",
                        read('pytest_httpretty.py'), re.M).group(1)


setup(name='pytest-httpretty',
      version=__version__,
      description='A thin wrapper of HTTPretty for pytest',
      author='papaeye',
      author_email='papaeye@gmail.com',
      url='http://github.com/papaeye/pytest-httpretty',
      py_modules=['pytest_httpretty'],
      include_package_data=True,
      install_requires=[
          'httpretty',
          'pytest',
      ],
      tests_require=[
          'requests'
      ],
      zip_safe=False,
      keywords='pytest httpretty http stub mock',
      classifiers=[
          'Development Status :: 3 - Alpha',
          'License :: OSI Approved :: BSD License',
          'Operating System :: OS Independent',
          'Programming Language :: Python',
          'Programming Language :: Python :: 2',
          'Programming Language :: Python :: 2.7',
          'Programming Language :: Python :: 3',
          'Programming Language :: Python :: 3.3',
      ],
      platforms='any',
      license='BSD License',
      entry_points={
          'pytest11': ['httpretty = pytest_httpretty']
      })
