# -*- coding: utf-8 -*-
"""
Created on Sat Apr  4 22:43:49 2020

@author: Rodrigo
"""

class Solution:
    def defangIPaddr(self, address: str) -> str:
        result = ""
        for key in address:
            if key == ".":
                result = result + "[.]"
            else:
                result = result + key
        return (result)