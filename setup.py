# Upload package to PyPi.

from setuptools import setup

setup(name='mebots',
      version='0.1.4',
      description='Library for running GroupMe bots with the MeBots API toolkit.',
      url='https://github.com/ErikBoesen/mebots.py',
      author='Erik Boesen',
      author_email='me@erikboesen.com',
      license='GPL',
      packages=['gmbots'],
      install_requires=['requests'])
