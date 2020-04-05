# -*- coding: utf-8 -*-
"""
Created on Sat Apr  4 22:44:28 2020

@author: Rodrigo
"""

class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        result = []
        i = 0
        for num in nums:
            for r in nums:
                if r < num:
                    i += 1
            result.append(i)
            i = 0
        return(result)