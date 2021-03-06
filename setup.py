import os

from setuptools import find_packages, setup

with open(os.path.join(os.path.dirname(__file__), 'README.md')) as readme:
    README = readme.read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='kivy.garden.progressspinner',
    version='0.1',
    packages=find_packages(),
    include_package_data=True,
    description='Fork of kivy-garden progress spinner',
    long_description=README,
    install_requires=[
        'kivy>=1.11.1',
    ]
)
