# -*- coding: utf-8 -*-
"""
Created on Wed Feb 26 17:16:27 2020

@author: roryw
"""

"""
Fle handling in python - Pyhton can create, open, close, read from and write
to files.
"""

f = open("kipling.txt", "w")
print(type(f))

f.write("If you can keep your head while all about you \n\
        are losing theirs and blaming it on you,\n")
f.write("If you can trust yourself when all men doubt you,\n\
        But make allowence for their doubting too;\n")
f.write("If you can wait and not be tired by waiting,\n\
        Or being lied about, don't deal in lies,\n")
f.write("Or being hated, don't give way to hating,\n\
        And yet don't look too good, nor talk too wise:\n")
f.close()

f = open("kipling.txt", "r")
print(type(f))
print(f.read())
f.close()

print()

f = open("kipling.txt", "r")
print(f.readline())
f.close()

"""
The readlines() method will return a list of strings in order, each element 
corresponding to a line in in the original file.
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
N.B. readlines() will continue from the CURRENT POSITION in the file, i.e.:
"""
f = open("kipling.txt", "r")
print(f.readlines())
f.close()

print()

f = open("kipling.txt", "r")
print(f.readline())
print(f.readlines())
f.close()

print()

f = open("kipling.txt", "r")
print(f.readline())
print(f.readline())
print(f.readlines())
f.close()
