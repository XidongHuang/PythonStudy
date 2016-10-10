"""*************************************************************************
    > File Name: ex44c_super.py
    > Author: XidongHuang (Tony)
    > Mail: xidonghuang@gmail.com 
    > Created Time: Sun  9 Oct 22:02:42 2016
 ************************************************************************"""

# -*- coding: utf-8 -*-

class Parent(object):

	def altered(self):
		print("PARENT altered()")

class Child(Parent):

	def altered(self):
		print("CHILD, BEFORE PARENT altered()")
		super(Child, self).altered()
		print("CHILD, AFTER PARENT altered()")

dad = Parent()
son = Child()

dad.altered()
son.altered()
