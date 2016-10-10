"""*************************************************************************
    > File Name: ex44_composition.py
    > Author: XidongHuang (Tony)
    > Mail: xidonghuang@gmail.com 
    > Created Time: Sun  9 Oct 23:35:27 2016
 ************************************************************************"""

# -*- coding: utf-8 -*-

class Other(object):

	def override(self):
		print("OTHER override()")

	def implicit(self):
		print("OTHER implicit()")

	def altered(self):
		print("OTHER altered()")

class Child(object):

	def __init__(self):
		self.other = Other()

	def implicit(self):
		self.other.implicit()

	def override(self):
		print("CHILD override()")

	def altered(self):
		print("CHILD, BEFORE OTHER altered()")

	def altered(self):
		print("CHILD, BEFORE OTHER altered()")
		self.other.altered()
		print("CHILD, AFTER OTHER altered()")

son = Child()

son.implicit()
son.override()
son.altered()
