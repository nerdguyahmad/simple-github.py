from setuptools import setup, find_packages

setup(name='simplegithub.py',
      author='nerdguyahmad',
      url='https://github.com/nerdguyahmad/simple-github.py',
      version='v1.0.0',
      packages='simplegithub/*',
      license='MIT',
      description='A highly simple (experimental) wrapper for basic operations with GitHub API.',
      install_requires=['requests'],
      python_requires='>=3.5.3'
)
