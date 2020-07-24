# SPDX-License-Identifier: AGPL-3.0-or-later
from distutils.command.build_py import build_py
from setuptools import setup, find_packages

setup(name='kopano-cli',
      version='1.0',
      url='https://github.com/kopano-cli',
      description='Improved Kopano admin utility built on python-kopano',
      author='Kopano',
      author_email='mark.dufour@gmail.com',
      keywords=['kopano'],
      license='AGPL',
      packages=find_packages(),
      install_requires=[
      ],
      scripts=['kopano-cli'],
)
