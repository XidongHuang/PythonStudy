"""*************************************************************************
    > File Name: ex8.py
    > Author: XidongHuang (Tony)
    > Mail: xidonghuang@gmail.com 
    > Created Time: Wed 28 Sep 16:27:02 2016
 ************************************************************************"""

# -*- coding: utf-8 -*-

formatter = "%r %r %r %r"
print(formatter % (1, 2, 3, 4))
print(formatter % ('one', 'two', 'three', 'four'))
print(formatter % (True, False, False, True))
print(formatter % (formatter, formatter, formatter, formatter))
print(formatter %
	("I had this thing.",
	"But it did't sing.",
	"中文",
	"So I said goodnight.")
		)
