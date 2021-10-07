from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in landlord/__init__.py
from landlord import __version__ as version

setup(
	name="landlord",
	version=version,
	description="LANDLORD",
	author="JMG",
	author_email="grijalva10@gmail.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
