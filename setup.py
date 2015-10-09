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
    version='1.1.0',
    author="Martin Strohalm",
    maintainer='Martin Strohalm',
    ext_modules=[
        Extension('mspy.calculations', ['mspy/calculations.c'],)
    ],
    packages=["mspy"],
    include_package_data=True,
    include_dirs=[numpy.get_include()],
    install_requires=["numpy"],
)
