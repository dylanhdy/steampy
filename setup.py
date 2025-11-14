import sys

from setuptools import setup

version = '1.2.0'

setup(
    name='steampy',
    packages=['steampy'],
    version=version,
    description='A Steam lib for trade automation',
    license='MIT',
    url='https://github.com/dylanhdy/steampy',
    keywords=['steam', 'trade'],
    classifiers=[],
    install_requires=[
        "requests",
        "beautifulsoup4",
        "rsa",
    ],
)
