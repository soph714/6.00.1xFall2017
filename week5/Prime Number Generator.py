# -*- coding: utf-8 -*-
"""
Created on Thu Jan 18 15:34:14 2018

@author: Ted
"""

def genPrimes():
    yield 2
    primeList = [2]
    prime = 1
    while True:
        prime += 1
        if all(prime % p for p in primeList):
            primeList.append(prime)
            yield prime