from setuptools import setup, find_packages
from simplegithub import __version__

setup(name='simplegithub.py',
      author='nerdguyahmad',
      url='https://github.com/nerdguyahmad/simple-github.py',
      version=__version__,
      packages=find_packages(include=['simplegithub', 'simplegithub.*']),
      license='MIT',
      description='A highly simple (experimental) wrapper for basic operations with GitHub API.',
      install_requires=['requests'],
      python_requires='>=3.5.3'
)