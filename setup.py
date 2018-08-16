# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

with open('README.md') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='rftb',
    version='0.1.0',
    description="Romain's ToolBox",
    long_description=readme,
    author='Romain Fontugne',
    url='https://github.com/romain-fontugne/rftb',
    license=license,
    packages=find_packages(exclude=('tests', 'docs'))
)

