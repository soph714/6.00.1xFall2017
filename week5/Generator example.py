# -*- coding: utf-8 -*-
"""
Created on Wed Jan 17 21:49:34 2018

@author: Ted
"""

def genFib():
    fib1 = 1 #fib(n-1)
    fib2 = 0 #fib(n-2)
    while True:
        # fib(n) = fib(n-1) + fib(n-2)
        next = fib1 + fib2
        yield next
        fib2 = fib1
        fib1 = next
    