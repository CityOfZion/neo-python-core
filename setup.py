#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""The setup script."""

from setuptools import setup, find_packages
from pip.req import parse_requirements
from pip.download import PipSession

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

install_reqs = parse_requirements('requirements.txt', session=PipSession())
reqs = [str(ir.req) for ir in install_reqs]

setup(
    name='neocore',
    python_requires='>=3.4, <3.6',
    version='0.3.2',
    description="Core functionality of neo-python",
    long_description=readme + '\n\n' + history,
    author="City of Zion",
    author_email='python@cityofzion.io',
    url='https://github.com/CityOfZion/neo-python-core',
    packages=find_packages(include=['neocore']),
    include_package_data=True,
    install_requires=reqs,
    license="MIT license",
    zip_safe=False,
    keywords='neocore, neo, python, node',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
    ]
)
