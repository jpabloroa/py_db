# setup.py snippet
from setuptools import setup, find_packages

setup(
    name="py_db",
    version="1.3",
    packages=find_packages(),
    install_requires=[
        "mysql-connector-python==9.0.0",
        "psycopg2==2.9.9",
        "pyodbc==5.1.0",
    ],
    author="Juan Pablo Roa",
    description="A Python library to manage SQL databases and APIs with a unified interface.",
)
