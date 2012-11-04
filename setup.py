from setuptools import setup, find_packages

import asana

version = '0.7'

setup(
    name='pysana',
    version=version,
    author='Angus Burton',
    author_email='angus@angusb.com',
    url='http://github.com/angusb/pysana', # fix
    description='asana api wrapper',
    # long_description=open('./README.md', 'r').read(),
    # download_url=
    classifiers=[
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        # License
        ],
    packages=find_packages(),
    install_requires=[
        'requests',
    ],
    # License
    keywords='asana api',
)
