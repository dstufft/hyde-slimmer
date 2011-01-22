from setuptools import setup, find_packages

setup(name='hyde-slimmer',
version='0.0.1',
description='Html compression as post processor',
long_description=open('README.rst').read(),
author='Donald von Stufft',
author_email='donald.stufft@gmail.com',
url='http://github.com/dstufft/hyde-slimmer',
classifiers=[
  "Programming Language :: Python",
  "Development Status :: 4 - Beta",
  "Intended Audience :: Developers",
],
keywords='hyde html compressor',
zip_safe=False,
license='BSD',
install_requires=[
'setuptools',
'slimmer',
],
packages = find_packages(),
include_package_data = True,
)
