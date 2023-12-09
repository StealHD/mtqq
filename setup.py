from setuptools import setup, find_packages
setup(
    name='mqtt',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        'selenium', 'paho-mqtt'
    ],
)