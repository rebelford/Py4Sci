from setuptools import setup

setup(
    name="pack1",
    version="0.1",
    py_modules=["my_fun1"],  # Register individual Python files
    package_dir={"": "."},  # Look in the current directory
    author="Your Name",
    description="Custom functions for our Python class",
)
