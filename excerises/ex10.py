"""*************************************************************************
    > File Name: ex10.py
    > Author: XidongHuang (Tony)
    > Mail: xidonghuang@gmail.com 
    > Created Time: Wed 28 Sep 18:04:08 2016
 ************************************************************************"""

# -*- coding: utf-8 -*-
tabby_cat = '\tI\'m tabbed in.'
persian_cat = 'I\'m split\non a line.'
backslash_cat = "I'm \\ a \\ cat."

fat_cat = """
I'll do a list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
"""

print(tabby_cat)
print(persian_cat)
print(backslash_cat)
print(fat_cat)

while True:
	for i in ["/","-","|","\\","|"]:
		print("%r\r" % i,)
