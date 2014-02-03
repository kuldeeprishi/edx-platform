#!/usr/bin/env python

"""
Install bok-choy page objects for acceptance and end-to-end tests.
"""

import os
from setuptools import setup

VERSION = '0.0.1'
DESCRIPTION = "Bok-choy page objects for edx-platform"

# Pip 1.5 will try to install this package from outside
# the directory containing setup.py.
# To protect against this, we change the directory ourselves.
# This will not affect the parent process, so we do not
# bother changing it back when we're done.
os.chdir(os.path.dirname(os.path.realpath(__file__)))

setup(
    name='edxapp-pages',
    version=VERSION,
    author='edX',
    url='http://github.com/edx/edx-platform',
    description=DESCRIPTION,
    license='AGPL',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU Affero General Public License v3',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Software Development :: Testing',
        'Topic :: Software Development :: Quality Assurance'
    ],
    packages=['lms', 'studio']
)
