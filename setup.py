# -*- coding: utf-8 -*-

import os
import sys

import setuptools


if sys.argv[-1] == 'publish':
    os.system('python setup.py sdist upload')
    sys.exit()

readme = open('README.md').read()

setuptools.setup(
    name='webscraper',
    version='0.0.7',
    description='Set of utility libs',
    long_description=readme + '\n\n',
    author='Claude Gibert',
    author_email='claude.gibert@gmail.com',
    url='https://github.com/legibe/webscraper',
    packages=[
        'webscraper',
    ],
    package_dir={'webscraper': 'webscraper'},
    install_requires=[
        'beautifulsoup4>= 4.4.1',
        'PyYAML >= 3.11',
        'requests >= 2.10.0',
    ],
    license="Internal",
    zip_safe=False,
    keywords='web scraper',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: Internal',
        'Natural Language :: English',
        'Programming Language :: Python :: 2.7'
    ],
    test_suite='tests',
)
