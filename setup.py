#!/usr/bin/env python
from setuptools import setup
name = 'easyxml'
setup(
    name             = name,
    author           = 'Evan Wallace',
    url              = 'https://github.com/evanw/easyxml',
    version          = __import__(name).__version__,
    py_modules       = [name],
)
