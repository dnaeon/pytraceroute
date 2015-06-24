from __future__ import print_function

import re
import ast
import sys

from setuptools import setup, find_packages


_version_re = re.compile(r'__version__\s+=\s+(.*)')

with open('src/traceroute/__init__.py', 'rb') as f:
    version = str(ast.literal_eval(_version_re.search(
        f.read().decode('utf-8')).group(1))
    )

setup(
    name='pytraceroute',
    version=version,
    description='A simple Python traceroute(8) implementation',
    long_description=open('README.rst').read(),
    author='Marin Atanasov Nikolov',
    author_email='dnaeon@gmail.com',
    license='BSD',
    url='https://github.com/dnaeon/pytraceroute',
    download_url='https://github.com/dnaeon/pytraceroute/releases',
    package_dir={'': 'src'},
    packages=find_packages('src'),
    scripts=[
        'src/py-traceroute',
    ],
    install_requires=[
        'docopt >= 0.6.2',
    ]
)
