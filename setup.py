import sys
import numpy
from setuptools import setup
from distutils.extension import Extension

# Build on WIN using MinGW:
# python setup.py build --compiler=mingw32
# Copy calculations.pyd to mspy directory

# Build on Mac:
# python setup.py build
# Copy calculations.so to mspy directory


# make setup
setup(
    name='mspy',
    version='1.1.1',
    author="Martin Strohalm",
    maintainer='Witold Wolski',
    author_email="wewolski@gmail.com",
    ext_modules=[
        Extension('mspy.calculations', ['mspy/calculations.c'],)
    ],
    packages=["mspy"],
    include_package_data=True,
    include_dirs=[numpy.get_include()],
    description = 'fork of the mMass library mspy http://www.mmass.org/',
    url='https://github.com/wolski/mspy',
    install_requires=["numpy"],
    license="GPL"
)
