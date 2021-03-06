"""Treasure Data Driver for Python

pytd is a Python interface to Treasure Data data management platform. Unlike
the other official Treasure Data API libraries for Python, td-client-python and
pandas-td, pytd gives a direct access to their back-end query and storage
engines. The seamless connection allows your Python code to read and write a
large volume of data in a shorter time. It eventually makes your day-to-day
data analytics work more efficient and productive.
"""
import ast
import re


with open('pytd/version.py', 'rb') as f:
    version_re = re.compile(r'__version__\s+=\s+(.*)')
    VERSION = str(ast.literal_eval(version_re.search(
        f.read().decode('utf-8')).group(1)))

from os import path
with open(path.join(path.abspath(path.dirname(__file__)), 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

DISTNAME = 'pytd'
DESCRIPTION = 'Treasure Data Driver for Python'
LONG_DESCRIPTION = long_description or __doc__
AUTHOR = 'Arm Treasure Data'
AUTHOR_EMAIL = 'support@treasure-data.com'
MAINTAINER = AUTHOR
MAINTAINER_EMAIL = AUTHOR_EMAIL
LICENSE = 'Apache License 2.0'
URL = 'https://github.com/treasure-data/pytd'


def setup_package():
    from setuptools import setup, find_packages

    metadata = dict(
        name=DISTNAME,
        version=VERSION,
        description=DESCRIPTION,
        long_description=LONG_DESCRIPTION,
        long_description_content_type='text/markdown',
        author=AUTHOR,
        author_email=AUTHOR_EMAIL,
        maintainer=MAINTAINER,
        maintainer_email=MAINTAINER_EMAIL,
        license=LICENSE,
        url=URL,
        classifiers=['Development Status :: 3 - Alpha',
                     'Intended Audience :: Developers',
                     'License :: OSI Approved :: Apache Software License',
                     'Topic :: Database',
                     'Programming Language :: Python',
                     'Programming Language :: Python :: 3',
                     'Programming Language :: Python :: 3.5',
                     'Programming Language :: Python :: 3.6',
                     'Programming Language :: Python :: 3.7',
                     ],
        packages=find_packages(exclude=['*tests*']),
        install_requires=[
            'presto-python-client>=0.6.0',
            'pandas>=0.22.0',
            'td-client>=0.12.0',
            'pytz>=2018.5',
        ],
        extras_require={
            'spark': ['pyspark>=2.4.0', 'pyarrow>=0.11.0'],
        })

    setup(**metadata)


if __name__ == '__main__':
    setup_package()
