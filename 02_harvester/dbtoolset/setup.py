from setuptools import setup, find_packages
from dbtoolset import 

setup(
    name="mydatabasetool",
    version="0.2.0",
    packages=find_packages(),
    install_requires=[
        "pymysql>=1.1.0",
        "psycopg2>=2.9.9",
        "pyodbc>=5.0.1",
        "pytest>=7.4.3",
        "PyYAML>=6.0.1"
    ],
    cmdclass={
        "install": CreateSampleConfigs,
    }
)
