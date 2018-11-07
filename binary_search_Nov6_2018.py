# -*- coding: utf-8 -*-
"""
Created on Tue Nov  6 21:55:46 2018

@author: Xun Cao
"""
            
def binarySearch (arr,x):
    rightIndx= len(arr)-1
    leftIndx = 0
    while rightIndx > leftIndx:
        mid=int((rightIndx-leftIndx)/2)
        if arr[mid]==x:
            return mid
        elif arr[mid] > x:
            rightIndx=mid
            mid=int((rightIndx-leftIndx)/2)
        else:
            leftIndx=mid
            mid=int((rightIndx-leftIndx)/2)
    return -1
            
            
arr=[1,2,3,45,80]
binarySearch(arr,3)
arr=[1,3,6,9]
binarySearch(arr,3)
binarySearch([1],3)
binarySearch([1],3)