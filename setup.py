#!/usr/bin/env python
# -*- coding: utf-8 -*-
import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name='pyKG2Vec',
    version="0.0.1",
    author="Sujit Rokka Chhetri",
    author_email="sujitchhetri@gmail.com",
    description="A python library for Knowledge Graph Embedding",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Sujit-O/pyKG2Vec.git",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3.5",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)