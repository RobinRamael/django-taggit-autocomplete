# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

long_description = open('README.txt').read()

setup(
    name='django-taggit-autocomplete',
    version='0.2',
    description='Autocompletion for django-taggit',
    long_description=long_description,
    author='Robin Ramael',
    author_email='robin.ramael@gmail.com',
    url='http://github.com/RobinRamael/django-taggit-autocomplete/',
    packages=find_packages(),
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Framework :: Django',
    ],
    zip_safe=False,
)
