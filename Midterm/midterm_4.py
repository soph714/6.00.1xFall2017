# -*- coding: utf-8 -*-
"""
Created on Sun Oct 15 14:21:19 2017

@author: Ted
"""

def getSublists(L, n):
    
    '''
    code by theosopher 10/15/2017
    6.00.1x MITx edX miterm problem 4
    
    assume L is not empty
    assume 0 < n <= len(L)
    
    '''
    sublists = []  
    
    for char in range(len(L)-n+1):
        print(L[char:char+n])
        sublists.append(L[char:char+n])
        
    print(sublists)
    return
            
        