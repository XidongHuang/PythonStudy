"""*************************************************************************
    > File Name: ex44d_IOS.py
    > Author: XidongHuang (Tony)
    > Mail: xidonghuang@gmail.com 
    > Created Time: Sun  9 Oct 22:11:27 2016
 ************************************************************************"""

# -*- coding: utf-8 -*-

class Parent(object):

	def override(self):
		print("PARENT override()")

	def implicit(self):
		print("PARENT implicit()")

	def altered(self):
		print("PARENT altered()")

class Child(Parent):

	def override(self):
		print("CHILD override()")

	def altered(self):
		print("CHILD, BEFORE PARENT altered()")
		super(Child, self).altered()
		print("CHILD, AFTER PARENT altered()")

dad = Parent()
son = Child()

dad.implicit()
son.implicit()

dad.override()
son.override()

dad.altered()
son.altered()
