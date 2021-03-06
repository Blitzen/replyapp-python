#!/usr/bin/env python

import os
import sys

try:
  from setuptools import setup
except ImportError:
  from distutils.core import setup

if sys.argv[-1] == 'publish':
  os.system('python setup.py sdist upload')
  sys.exit()

requires = [
  'requests==2.6.0'
]

setup(
  name='replyapp-python',
  version='0.2.0',
  description='Python 3 api wrapper for replyapp.io',
  author='Jordan Clark',
  author_email='jordan@blitzen.com',
  url='https://github.com/Blitzen/replyapp-python',
  packages=['replyapp'],
  install_requires=requires,
  license='MIT',
  zip_safe=False,
  classifiers=(
    'Development Status :: 4 - Beta',
    'Intended Audience :: Developers',
    'Natural Language :: English',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3',
  )
)
