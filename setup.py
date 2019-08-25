# Upload package to PyPi.

from setuptools import setup

setup(name='gmbots',
      version='0.1.4',
      description='Library for interacting with the GMBots hosted GroupMe bot toolkit.',
      url='https://github.com/ErikBoesen/gmbotspy',
      author='Erik Boesen',
      author_email='me@erikboesen.com',
      license='GPL',
      packages=['gmbots'],
      install_requires=['requests'])
