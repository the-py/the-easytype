#!/usr/bin/env python

from setuptools import setup

def readme():
    with open("README.rst") as it:
        return it.read()

if __name__ == '__main__':
    setup(
        name = 'theeasytype',
        version = '0.0.1',
        description = '`the` assert basic type',
        long_description = readme(),
        author = "Yan Wenjun",
        author_email = "mylastnameisyan@gmail.com",
        license = 'MIT',
        url = 'https://github.com/the-py/the-easytype',
        py_modules = ["theeasytype"],
        classifiers = [
            'License :: OSI Approved :: MIT License',
            'Topic :: Software Development :: Libraries',
        ]
    )
