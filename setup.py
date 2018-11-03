#    Copyright 2017 - 2018 Ruben Decrop
#
#    Licensed under the Apache License, Version 2.0 (the "License");
#    you may not use this file except in compliance with the License.
#    You may obtain a copy of the License at
#
#        http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS,
#    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#    See the License for the specific language governing permissions and
#    limitations under the License.


import os

from setuptools import setup, find_packages

requires = []

setup(
    name='rd_django',
    version='0.7.0',
    description='Reddevil django addons',
    long_description='Reddevil django addons',
    classifiers=[
        "Programming Language :: Python",
        "Framework :: Django-cms",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Internet :: WWW/HTTP :: WSGI :: Application",
    ],
    author='Ruben Decrop',
    author_email='ruben@decrop.net',
    keywords='Reddevil',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
)
