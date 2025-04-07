from setuptools import setup, find_packages

setup(
    name="my_pack",
    version="0.1",
    packages=find_packages(),  # ✅ Looks for __init__.py to find packages
    author="Bob Belford",
    description="Custom functions for our Python class",
)
