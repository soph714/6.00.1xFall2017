# -*- coding: utf-8 -*-
"""
Created on Wed Nov  1 18:36:41 2017

@author: Ted
"""

def getWordScore(word, n):
    """
    code by: tjs on 11/1/2017 for MITx edX 6.00.1x pset4.1    
    
    
    Returns the score for a word. Assumes the word is a valid word.

    The score for a word is the sum of the points for letters in the
    word, multiplied by the length of the word, PLUS 50 points if all n
    letters are used on the first turn.

    Letters are scored as in Scrabble; A is worth 1, B is worth 3, C is
    worth 3, D is worth 2, E is worth 1, and so on (see SCRABBLE_LETTER_VALUES)

    word: string (lowercase letters)
    n: integer (HAND_SIZE; i.e., hand size required for additional points)
    returns: int >= 0
    """
    
    SCRABBLE_LETTER_VALUES = {
    'a': 1, 'b': 3, 'c': 3, 'd': 2, 'e': 1, 'f': 4, 'g': 2, 'h': 4, 'i': 1, 'j': 8, 'k': 5, 'l': 1, 'm': 3, 'n': 1, 'o': 1, 'p': 3, 'q': 10, 'r': 1, 's': 1, 't': 1, 'u': 1, 'v': 4, 'w': 4, 'x': 8, 'y': 4, 'z': 10
}
    
    wordScore = 0
    # wordScore used to keep track of total score of words
    
    for letter in word:
        if letter in SCRABBLE_LETTER_VALUES.keys():
            wordScore += SCRABBLE_LETTER_VALUES[letter]
    # iterating over each letter in word and summing the values into wordScore
    
    wordScore *= len(word)
    # multiplying word length to wordScore
    
    if len(word) == n:
        wordScore += 50
    # if all letters are used in the word 50 points are added to the total
    
    return wordScore
        
    
    
    
    
    # TO DO ... <-- Remove this comment when you code this function

