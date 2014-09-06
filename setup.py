# -*- coding: utf-8 -*-
#!/usr/bin/env python

import os
import sys


try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

import serverpi
version = serverpi.__version__

setup(
    name='ServerPi',
    version=version,
    author='',
    author_email='richard@richard-fellows.com',
    packages=[
        'serverpi',
    ],
    include_package_data=True,
    install_requires=[
        'Django>=1.6.5',
    ],
    zip_safe=False,
    scripts=['serverpi/manage.py'],
)