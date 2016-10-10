"""*************************************************************************
    > File Name: ex44a_inheritance.py
    > Author: XidongHuang (Tony)
    > Mail: xidonghuang@gmail.com 
    > Created Time: Sun  9 Oct 21:57:10 2016
 ************************************************************************"""

# -*- coding: utf-8 -*-

class Parent(object):

	def implicit(self):
		print("PARENT implicit()")

class Child(Parent):
	pass

dad = Parent()
son = Child()

dad.implicit()
son.implicit()
