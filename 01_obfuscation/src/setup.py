from setuptools import setup, find_packages

setup(
    name="pymalware-obfuscation",
    version="1.0.0",
    packages=find_packages(),
    author="Leonid Akinin (fatzy)",
    author_email="fatzy@protonmail.com",
    description="Collection of obfuscation techniques for python malware",
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
