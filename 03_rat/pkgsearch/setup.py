from setuptools import setup, find_packages
import os

version = {}
with open("pkg_search/version.py") as fp:
    exec(fp.read(), version)

setup(
    name="pkg-search",
    version=version["__version__"],
    packages=find_packages(),
    install_requires=[
        "requests",
        "beautifulsoup4",
    ],
    entry_points={
        "console_scripts": [
            "pkg-search=pkg_search.cli:main",
        ],
    },
    author="Your Name",
    author_email="your.email@example.com",
    description="CLI utility to search for packages across different managers",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/pkg-search",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
