# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

setup(
    name='bgapi',
    version='0.0.2',
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
    packages=find_packages(exclude=['contrib', 'docs', 'tests']),
    author='Arthur Crippa Búrigo',
    author_email='arthurcburigo@gmail.com',
)
