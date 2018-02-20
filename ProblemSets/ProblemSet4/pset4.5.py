# -*- coding: utf-8 -*-
"""
Created on Thu Nov  9 19:52:11 2017

@author: Ted
"""

def playHand(hand, wordList, n):
    """
    
    code by TJS for edx MITx 6.00.1x pset4.5 on 11/9/2017    
    
    Allows the user to play the given hand, as follows:

    * The hand is displayed.
    * The user may input a word or a single period (the string ".") 
      to indicate they're done playing
    * Invalid words are rejected, and a message is displayed asking
      the user to choose another word until they enter a valid word or "."
    * When a valid word is entered, it uses up letters from the hand.
    * After every valid word: the score for that word is displayed,
      the remaining letters in the hand are displayed, and the user
      is asked to input another word.
    * The sum of the word scores is displayed when the hand finishes.
    * The hand finishes when there are no more unused letters or the user
      inputs a "."

      hand: dictionary (string -> int)
      wordList: list of lowercase strings
      n: integer (HAND_SIZE; i.e., hand size required for additional points)
      
    """
    # BEGIN PSEUDOCODE <-- Remove this comment when you code this function; do your coding within the pseudocode (leaving those comments in-place!)
    
    totalScore = 0
    # Keep track of the total score
    updatedN = n
    while updatedN > 0:
    # As long as there are still letters left in the hand:
        
        print("Current Hand: ",end=" ")
        displayHand(hand)
        # Display the hand
        
        enterWord = input('Enter word, or a "." to indicate that you are finished: ')
        # Ask user for input
        
        if enterWord == '.':
        # If the input is a single period:
            print("Goodbye! Total score: ",totalScore)
            return
            # break
            # End the game (break out of the loop)

        else:
        # Otherwise (the input is not a single period):
            if isValidWord(enterWord, hand, wordList) == False:
            # If the word is not valid:
                print("Invalid word, please try again. \n")
                # Reject invalid word (print a message followed by a blank line)
            else:
            # Otherwise (the word is valid):
                totalScore += getWordScore(enterWord, n)
                updatedN -= len(enterWord)
                print(enterWord," earned ",getWordScore(enterWord, n)," points. Total score: ",totalScore,"\n")
                # Tell the user how many points the word earned, and the updated total score, in one line followed by a blank line
                hand = updateHand(hand, enterWord)
                # Update the hand 
                
    print("Run out of letters. Total score: ",totalScore," points.")
    return
        
    # Game is over (user entered a '.' or ran out of letters), so tell user the total score

