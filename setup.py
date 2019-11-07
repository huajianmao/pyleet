# -*- coding: utf-8 -*-

from setuptools import setup, find_packages


with open('README.md') as f:
    readme = f.read()

with open('LICENSE') as f:
    mylicense = f.read()

setup(
    name='Leetcode',
    version='0.1.0',
    description='Leetcode solutions in Python 3',
    long_description=readme,
    author='Huajian Mao',
    author_email='huajianmao@gmail.com',
    url='https://github.com/huajianmao/pyleet',
    license=mylicense,
    packages=find_packages(exclude=('tests', 'docs'))
)
