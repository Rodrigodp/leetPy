# -*- coding: utf-8 -*-
"""
Created on Sun Apr  5 14:23:58 2020

@author: Rodrigo
"""

import unittest

class Solution:
    def decompressRLElist(self, nums: list) -> list:
        tt = [nums[i:i+2] for i in range(0,len(nums),2)]
        result = []
        for par in tt:
            freq = par[0]
            val = par[1]
            while freq != 0:
                result.append(val)
                freq -= 1
        return(result)

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(Solution.decompressRLElist(self,[1,1,2,3]),[1,3,3])

if __name__ == '__main__': 
    unittest.main()