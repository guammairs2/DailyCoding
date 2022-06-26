'''
Get product of all other elements

Given an array of intgers, return a new array such that each 
<<<<<<< HEAD
element at index i of the new array is the product of all the 
=======
element at index i of the new arry is the product of all the 
>>>>>>> 9f862abbf596d09129280349b3e313bb70eb8b58
numbers in the original array except the one at i.
'''
from math import prod

def findprod(lister):

    return [int(prod(lister)/lister[i]) for i in range(0,len(lister))]

<<<<<<< HEAD
'''
Follow-up: What if you can't use division?

To do this we will precompute results from subarrays, and then build
up a solution from these results.
'''

def products(nums):
    # Generate prefix products
    prefix_products = []
    for num in nums:
        if prefix_products:
            prefix_products.append(prefix_products[-1] * num)
        else:
            prefix_products.append(num)

    # Generate suffix products
    suffix_products = []
    for num in reversed(nums):
        if suffix_products:
            suffix_products.append(suffix_products[-1] * num)
        else:
            suffix_products.append(num)
    suffix_products = list(reversed(suffix_products))

    # Generate result from product of prefixes and suffixes
    result = []
    for i in range(len(nums)):
        if i == 0:
            result.append(suffix_products[i+1])
        elif i == len(nums) - 1:
            result.append(prefix_products[i-1])
        else:
            result.append(
                prefix_products[i - 1] * suffix_products[i + 1]
            )
    return result

'''
This runs in O(n) time and space, since iterating over the input array 
takes O(n) time and the prefix and suffix arrays take up O(n) space
'''

if __name__ == '__main__':
    a = [1,2,3,4,5]

    print(products(a))
=======
>>>>>>> 9f862abbf596d09129280349b3e313bb70eb8b58
