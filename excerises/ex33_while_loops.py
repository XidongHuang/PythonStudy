"""*************************************************************************
    > File Name: ex33_while_loops.py
    > Author: XidongHuang (Tony)
    > Mail: xidonghuang@gmail.com 
    > Created Time: Sun  2 Oct 17:01:06 2016
 ************************************************************************"""

# -*- coding: utf-8 -*-

i = 0
numbers = []

while i < 6:
	print("At the end top i is %d" % i)
	numbers.append(i)

	i = i + 1
	print("Numbers now: ", numbers)
	print("At the bottom i is %d" % i)

print("The numbers: ")

for num in numbers:
	print(num)
