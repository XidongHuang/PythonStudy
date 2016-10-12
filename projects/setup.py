"""*************************************************************************
    > File Name: setup.py
    > Author: XidongHuang (Tony)
    > Mail: xidonghuang@gmail.com 
    > Created Time: Tue 11 Oct 23:01:26 2016
 ************************************************************************"""

# -*- coding: utf-8 -*-

try:
	from setuptools import setup

except ImportError:
	from distutils.core import setup

config = {
		'description': 'My first Python project',
		'author': 'Tony',
		'url': 'URL to get it at.',
		'download_url': 'Where to download it.',
		'author_email': 'xidonghuang@gmail.com',
		'version': '0.1',
		'install_requires': ['nose'],
		'packages': ['NAME'],
		'script': [],
		'name': 'hello_world'

		}
		
setup(**config)
