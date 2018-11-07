# -*- coding: utf-8 -*-
"""
Created on Tue Nov  6 23:19:51 2018

@author: Xun Cao
"""

class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        right=len(numbers)-1
        left=0
        while left < right:
            if numbers[right]+numbers[left]==target:
                return left+1,right+1
            elif numbers[right]+numbers[left]>target:
                right=right-1
            else:
                left=left+1
