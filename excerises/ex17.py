"""*************************************************************************
    > File Name: ex17.py
    > Author: XidongHuang (Tony)
    > Mail: xidonghuang@gmail.com 
    > Created Time: Wed 28 Sep 20:07:52 2016
 ************************************************************************"""

# -*- coding: utf-8 -*-

from sys import argv
from os.path import exists

script, from_file, to_file = argv

print("Copying from %s to %s" % (from_file, to_file))

# we could do these two on one line too, how?
in_file = open(from_file).read()
#indata = in_file.read()

print("The input file is %d bytes long" % len(in_file))

print("Does the output file exist? %r" % exists(to_file))
print("Ready, hit RETURN to continue, CTRL-C to abort.s")
input("? ")

out_file = open(to_file, 'w')
out_file.write(in_file)

print("Alright, all done.")

out_file.close()
#in_file.close()
