# -*- coding: utf-8 -*-
"""
Created on Sat Apr  4 22:43:16 2020

@author: Rodrigo
"""
import unittest

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
        
class Teste(unittest.TestCase):
    def test(self):
        self.assertEqual(Solution.numberOfSteps(self, 14),6)

if __name__ == '__main__': 
    unittest.main() 
