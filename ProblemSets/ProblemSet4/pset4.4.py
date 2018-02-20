# -*- coding: utf-8 -*-
"""
Created on Wed Nov  8 21:52:08 2017

@author: Ted
"""

def calculateHandlen(hand):
    """ 
    code by TJS for edX MITx 6.00.1x pset4.4 on 11/8/2017
    
    Returns the length (number of letters) in the current hand.
    
    hand: dictionary (string-> int)
    returns: integer
    """
    
    handCount = 0
    for letter in hand:
        handCount += hand[letter]
    return handCount
    
    
    
    
    
    
    
    
    
    