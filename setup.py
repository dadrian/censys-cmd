# -*- coding: utf-8 -*-

import os
from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))

setup(
    name='censys-cmd',
    version="0.0.1",
    description='Command-line tools for interacting with the Censys Search Engine (censys.io)',
    long_description='Command-line tools for interacting with the Censys Search Engine (censys.io)',
    classifiers=[
        "Programming Language :: Python",
    ],
    author="David Adrian",
    author_email="davidcadrian@gmail.com",
    license="Apache License, Version 2.0",
    url='https://github.com/dadrian/censys-cmd',
    keywords='censys',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        "censys",
    ],
    entry_points={
        'console_scripts': [
            'censys = censyscmd.__main__:main',
        ]
    }
)
