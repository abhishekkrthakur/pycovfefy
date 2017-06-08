#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup

with open('README.md') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = [
    'Click>=6.0',
    # TODO: put package requirements here
]

test_requirements = [
    # TODO: put package test requirements here
]

setup(
    name='pycovfefy',
    version='0.1.0',
    description="Python package to covfefy any string.",
    long_description=readme + '\n\n' + history,
    author="Pycovfefy",
    author_email='abhishek4@gmail.com',
    url='https://github.com/pycovfefy/pycovfefy',
    packages=[
        'pycovfefy',
    ],
    package_dir={'pycovfefy':
                 'pycovfefy'},
    entry_points={
        'console_scripts': [
            'pycovfefy=pycovfefy.cli:main'
        ]
    },
    include_package_data=True,
    install_requires=requirements,
    license="MIT license",
    zip_safe=False,
    keywords='pycovfefy',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
    ],
    test_suite='tests',
    tests_require=test_requirements
)
