from setuptools import setup, find_packages
from setuptools.command.install import install
import os, base64, json

setup(
    name="dbtoolset",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "pymysql>=1.1.0",
        "pyodbc>=5.0.1",
        "pytest>=7.4.3",
    ],
    author="Leonid Akinin (fatzy)",
    author_email="fatzy@protonmail.com",
    description="Collection of connectors for various DBs",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/pkg-search",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.8",
)
