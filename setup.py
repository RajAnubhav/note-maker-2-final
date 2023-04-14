from setuptools import setup, find_packages

setup(
    name='mysite',
    version='1.0',
    packages=find_packages(),
    install_requires=[
        'Django',
        # add any other dependencies here
    ],
)