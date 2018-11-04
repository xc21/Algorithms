# -*- coding: utf-8 -*-
"""
Created on Sun Nov  4 09:31:56 2018

@author: Xun Cao
"""


#Arrary
#Q1: your input is to reoder the arrary of integers, and you have to make even number appear first
# do it in O(1) space

#Strategy: take the advance of the both ends of the arrary,
#start from two ends, do the swaping

def even_odd(A):
    next_even=0
    next_odd=len(A)-1
    while next_even < next_odd:
        if A[next_even] % 2 == 0:
            next_even += 1
        else:
          A[next_even]=  A[next_odd]
          A[next_odd]=  A[next_even]
          next_odd-=1
