import setuptools
from setuptools import setup

setup(
    name='dsp',
    version='0.1',
    description='DSP scripts',
    python_requires='>=3.6',
    install_requires=[
        'matplotlib',
        'numpy',
        'pandas',
        'pyyaml',
        'scipy',
    ],
)
