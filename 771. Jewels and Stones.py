# -*- coding: utf-8 -*-
"""
Created on Sat Apr  4 22:36:41 2020

@author: Rodrigo
"""

class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        i = 0
        for jewels in J:
            for stones in S:
                if jewels == stones:
                    i = i + 1
        return(i)