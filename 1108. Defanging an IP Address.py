# -*- coding: utf-8 -*-
"""
Created on Sat Apr  4 22:43:49 2020

@author: Rodrigo
"""
import unittest

class Solution:
    def defangIPaddr(self, address: str) -> str:
        result = ""
        for key in address:
            if key == ".":
                result = result + "[.]"
            else:
                result = result + key
        return (result)
    
class Teste(unittest.TestCase):
    def test(self):
        self.assertEqual(Solution.defangIPaddr(self, "1.1.1.1"),'1[.]1[.]1[.]1')

if __name__ == '__main__': 
    unittest.main() 

