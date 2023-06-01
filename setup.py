"""
pinger
-------------

check connection status of various services
"""
from setuptools import setup, find_packages
from os import path

import versioneer

this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, "README.md"), encoding="utf-8") as f:
    long_description = f.read()

with open("requirements/production.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="pinger",
    version=versioneer.get_version(),
    cmdclass=versioneer.get_cmdclass(),
    description="check connection status of various services",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="http://github.com/a6enez3r-sidefx/pinger",
    author="Abenezer Mamo",
    author_email="hi@abenezer.sh",
    license="MIT",
    packages=find_packages(exclude=("tests", "env")),
    install_requires=requirements,
    zip_safe=False,
)
