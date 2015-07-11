#!/usr/bin/env python

from setuptools import setup, find_packages

packages = find_packages()

setup(
    name='cooperhewitt.api.multiclient',
    namespace_packages=['cooperhewitt', 'cooperhewitt.api', 'cooperhewitt.api.multiclient'],
    version='0.1',
    description='Python bindings to the Cooper-Hewitt collections API with support for multiple parallel requests (using grequests).',
    author='Smithsonian Cooper-Hewitt National Design Museum',
    url='https://github.com/cooperhewitt/py-cooperhewitt-api-multiclient',
    install_requires=[
        'cooperhewitt.api',
        'grequests',
        ],
    dependency_links=[
        'https://github.com/cooperhewitt/py-cooperhewitt-api/tarball/master#egg=cooperhewitt-api-0.4.4',
      ],
    packages=packages,
    scripts=[],
    download_url='https://github.com/cooperhewitt/py-cooperhewitt-api-multiclient/releases/tag/v0.1',
    license='BSD')
