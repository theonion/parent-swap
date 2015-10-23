# -*- coding: utf-8 -*-
import os
from setuptools import setup

name = 'parent_swap'
version = '0.0.1'

# allow setup.py to be run from any path
os.chdir(
    os.path.normpath(
        os.path.join(os.path.abspath(__file__), os.pardir)
    )
)

install_requires = [
    "django>=1.7,<1.9"
]

setup(
    name=name,
    version=version,
    description='Replace abstract parent classes of django objects',
    license='MIT',
    author='Cameron Lowe',
    author_email='clowe@theonion.com',
    include_package_data=True,
    install_requires=install_requires,
    test_suite='parent_swap.tests.runtests.main',
    packages=[
        'parent_swap'
    ],
)
