import os.path

from setuptools import setup


here = os.path.dirname(os.path.abspath(__file__))
version = next((line.split('=')[1].strip().replace("'", '')
                for line in open(os.path.join(here, 'pytest_httpretty.py'))
                if line.startswith('__version__ = ')),
               '0.0.0.dev0')


setup(name='pytest-httpretty',
      version=version,
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
