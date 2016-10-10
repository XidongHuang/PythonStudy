"""*************************************************************************
    > File Name: ex44b_override.py
    > Author: XidongHuang (Tony)
    > Mail: xidonghuang@gmail.com 
    > Created Time: Sun  9 Oct 21:59:36 2016
 ************************************************************************"""

# -*- coding: utf-8 -*-

class Parent(object):

	def override(self):
		print("PARENT override()")

class Child(Parent):

	def override(self):
		print("CHILD override()")

dad = Parent()
son = Child()

dad.override()
son.override()
