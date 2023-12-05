# -*- coding: utf-8 -*-
"""
Created on Tue Dec  5 14:43:56 2023

@author: HP
"""


def shortestPalindrome(s):
    i = 0
    for j in range(len(s) - 1, -1, -1):
        if s[i] == s[j]:
            i += 1
    
    if i == len(s):
        return s
    
    suffix = s[i:]
    prefix = suffix[::-1]
    
    return prefix + shortestPalindrome(s[:i]) + suffix

