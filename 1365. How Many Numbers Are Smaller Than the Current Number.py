# -*- coding: utf-8 -*-
"""
Created on Sat Apr  4 22:44:28 2020

@author: Rodrigo
"""
import unittest

class Solution:
    def smallerNumbersThanCurrent(self, nums: list) -> list:
        result = []
        i = 0
        for num in nums:
            for r in nums:
                if r < num:
                    i += 1
            result.append(i)
            i = 0
        return(result)
        
            
class Teste(unittest.TestCase):
    def test(self):
        self.assertEqual(Solution.smallerNumbersThanCurrent(self,[8,1,2,2,3]),[4,0,1,1,3])

if __name__ == '__main__': 
    unittest.main() 