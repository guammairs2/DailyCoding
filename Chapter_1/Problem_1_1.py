'''
Get product of all other elements

Given an array of intgers, return a new array such that each 
element at index i of the new arry is the product of all the 
numbers in the original array except the one at i.
'''
from math import prod

def findprod(lister):

    return [int(prod(lister)/lister[i]) for i in range(0,len(lister))]

