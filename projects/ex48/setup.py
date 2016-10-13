"""*************************************************************************
    > File Name: setup.py
    > Author: XidongHuang (Tony)
    > Mail: xidonghuang@gmail.com 
    > Created Time: Wed 12 Oct 18:25:20 2016
 ************************************************************************"""
#!/usr/bin/env python
# -*- coding: utf-8 -*-

try:
	from setuptools import setup

except ImportError:
	from distutils.core import setup

config = {
		'description':'Excerise 48, Advanced User Input',
		'author': 'Tony',
		'url': 'URL to get it at.',
		'download_url': 'Where to download it.',
		'author_email': 'xidonghuang@gmail.com',
		'version': '0.1',
		'install_requires': ['nose'],
		'packages': ['ex48'],
		'scripts': [],
		'name': 'ex48'
		}

setup(**config)
