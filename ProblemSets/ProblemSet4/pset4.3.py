# -*- coding: utf-8 -*-
"""
Created on Wed Nov  8 20:29:06 2017

@author: Ted
"""

def isValidWord(word, hand, wordList):
    """
    Code by TJS for edX MITx 6.00.1x pset4.3 on 11/8/2017
    
    Returns True if word is in the wordList and is entirely
    composed of letters in the hand. Otherwise, returns False.

    Does not mutate hand or wordList.
   
    word: string
    hand: dictionary (string -> int)
    wordList: list of lowercase strings
    """
    
    
    if type(word) != str:
        return False
    
    if word not in wordList:
        return False
    
    for letter in word:
        if letter not in hand:
            return False
    
    updatedHand = hand.copy()
    # copy hand as to not mutate the hand passed in
    
    for letter in word:
        if letter in updatedHand:
            updatedHand[letter] -= 1
            
    for letter in word:
        if updatedHand[letter] < 0:
            return False
        
    return True
