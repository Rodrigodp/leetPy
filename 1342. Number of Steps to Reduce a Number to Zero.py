# -*- coding: utf-8 -*-
"""
Created on Sat Apr  4 22:43:16 2020

@author: Rodrigo
"""

class Solution:
    def numberOfSteps (self, num: int) -> int:
        i = 0
        while num > 0:
            if num % 2 != 0:
                num = num - 1
                i = i + 1
            else: 
                num = num/2
                i = i + 1
        return(i)