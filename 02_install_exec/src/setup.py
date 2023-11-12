from setuptools import setup, find_packages

setup(
    name="nettools-ultra",
    version="1.0.0",
    packages=find_packages(),
    install_requires=[
        "requests>=2.31.0",
    ],
    entry_points={
        "console_scripts": [
            "nettools=net_tools.cli:main",
            "whoami=net_tools.utils:whoami",
        ],
    },
    author="Your Name",
    author_email="your.email@example.com",
    description="CLI utility for various network operations",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/pypa/sampleproject",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.8",
)