# -*- coding: utf-8 -*-
"""
Created on Sun Oct 15 15:58:08 2017

@author: Ted
"""

def dict_invert(d):
    '''
    code by theosopher
    10/15/2017
    6.00.1x MITx edX midterm
        
    d: dict
    Returns an inverted dictionary according to the instructions above
    '''
    newD = {}
    for key in d.keys():
        if d[key] in newD:
            newD[d[key]].append(key)
            newD[d[key]] = sorted(newD[d[key]])
        else:
            newD[d[key]] = [key]
    return newD