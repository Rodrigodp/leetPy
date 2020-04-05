# -*- coding: utf-8 -*-
"""
Created on Sat Apr  4 22:36:41 2020

@author: Rodrigo
"""
import unittest

class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        i = 0
        for jewels in J:
            for stones in S:
                if jewels == stones:
                    i = i + 1
        return(i)
        
class Teste(unittest.TestCase):
    def test(self):
        self.assertEqual(Solution.numJewelsInStones(self, "aA","aAAbbbb"),3)

if __name__ == '__main__': 
    unittest.main() 
