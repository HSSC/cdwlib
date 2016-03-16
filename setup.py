#!/usr/bin/env python

from setuptools import setup

setup (
    setup_requires=['pbr'],
    pbr=True,
    package_dir={ 'cdwlib':'src' },
    packages=['cdwlib' ],
    test_suite='test'
)
