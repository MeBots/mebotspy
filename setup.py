# Upload package to PyPi.

from setuptools import setup

setup(name='mebots',
      version='0.2.0',
      description='Library for running GroupMe bots with the MeBots API toolkit.',
      url='https://github.com/MeBots/mebotspy',
      author='Erik Boesen',
      author_email='me@erikboesen.com',
      license='GPL',
      packages=['mebots'],
      install_requires=['requests'])
