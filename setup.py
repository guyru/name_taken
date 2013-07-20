#!/usr/bin/env python

import os
from distutils.core import setup

# Utility function to read the README file.
# Used for the long_description.  It's nice, because now 1) we have a top level
# README file and 2) it's easier to type in the README file than to put a raw
# string in below ...
def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name='name_taken',
    version='0.1',
    description='A simple script that check if a project name is already taken.',
    url='https://github.com/guyru/name_taken',
    author='Guy Rutenberg',
    author_email='guyrutenberg@gmail.com',
    license = 'GPLv2+',
    scripts=['name_taken.py'],
    long_description=read('README.md'),
)
