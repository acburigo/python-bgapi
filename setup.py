# -*- coding: utf-8 -*-

from setuptools import setup, find_packages
import time

PACKAGE = 'bgapi'
BASE_VERSION = '0.0.2'
IS_RELEASED = True
version = BASE_VERSION

if not IS_RELEASED:
    version = "{}.dev{}".format(BASE_VERSION, int(time.time()))

setup(
    name='bgapi',
    version=version,
    description='Library for creating and parsing BGAPI packets.',
    url='https://github.com/acburigo/python-bgapi',
    python_requires='>=3',
    license='MIT',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
    ],
    keywords=['BGAPI', 'protocol', 'encode', 'decode', 'ble',
              'bluetooth low energy'],
    package_dir={'': 'src'},
    packages=find_packages(where='src'),
    #packages=find_packages(exclude=['contrib', 'docs', 'tests']),
    zip_safe=False,
    author='Arthur Crippa Búrigo',
    author_email='arthurcburigo@gmail.com',
)
