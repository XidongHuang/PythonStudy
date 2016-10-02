"""*************************************************************************
    > File Name: ex30_else_and_if.py
    > Author: XidongHuang (Tony)
    > Mail: xidonghuang@gmail.com 
    > Created Time: Sun  2 Oct 11:08:44 2016
 ************************************************************************"""

# -*- coding: utf-8 -*-

people = 30
cars = 40
buses = 15

if cars > people:
	print("We should take the cars.")
elif cars < people:
	print("We should not take the cars.")
else:
	print("We can't decide.")

if buses > cars:
	print("That's too many buses.")
elif buses < cars:
	print("Maybe we could take the buses.")
else:
	print("We still can't decide.")

if people > buses:
	print("Alright, let's just take the buses.")
else:
	print("Fine, let's stay home then.")
