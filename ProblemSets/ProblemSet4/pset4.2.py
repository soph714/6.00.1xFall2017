# -*- coding: utf-8 -*-
"""
Created on Wed Nov  8 20:10:52 2017

@author: Ted
"""

def updateHand(hand, word):
    """
    Code by TJS on 11/8/2017 for edX MITx 6.00.1x pset 4.2
    
    Assumes that 'hand' has all the letters in word.
    In other words, this assumes that however many times
    a letter appears in 'word', 'hand' has at least as
    many of that letter in it. 

    Updates the hand: uses up the letters in the given word
    and returns the new hand, without those letters in it.

    Has no side effects: does not modify hand.

    word: string
    hand: dictionary (string -> int)    
    returns: dictionary (string -> int)
    """
    updatedHand = hand.copy()
    # copy hand as to not mutate the hand passed in
    
    for letter in word:
        if letter in updatedHand:
            updatedHand[letter] -= 1
    # iterates over each letter in word and subtracts 1 from value if in hand
    
    return updatedHand
    
    
    # TO DO ... <-- Remove this comment when you code this function


