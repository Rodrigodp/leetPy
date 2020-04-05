# -*- coding: utf-8 -*-
"""
Created on Sun Apr  5 19:10:39 2020

@author: Rodrigo
"""
import unittest


class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        ns = str(n)
        pr = 1
        sm = 0
        for d in ns:
            pr = pr * int(d)
            sm = sm + int(d)
        sub = pr - sm
        return(sub)

class Teste(unittest.TestCase):
    def test(self):
        self.assertEqual(Solution.subtractProductAndSum(self,4421),21)

if __name__ == '__main__': 
    unittest.main() 
