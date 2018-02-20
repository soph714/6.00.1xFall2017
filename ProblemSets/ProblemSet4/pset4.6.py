# -*- coding: utf-8 -*-
"""
Created on Mon Nov 13 12:55:14 2017

@author: sophert
"""
def playGame(wordList):
    
    # creating a function in a function to pass the oldHand through
    def playGameOld(wordList, oldHand):
        """
        written by TJS on 11/12/2017 for edX MITx 6.00.1x pset4.6
        
        Allow the user to play an arbitrary number of hands.
    
        1) Asks the user to input 'n' or 'r' or 'e'.
          * If the user inputs 'n', let the user play a new (random) hand.
          * If the user inputs 'r', let the user play the last hand again.
          * If the user inputs 'e', exit the game.
          * If the user inputs anything else, tell them their input was invalid.
     
        2) When done playing the hand, repeat from step 1    
        """
        
        # HAND_SIZE = 7
        # number of letters in hand, commented out, not needed
            
        gameStart = input('Enter n  to deal a new hand, r to replay the last hand, or e to end game: ')
            # get user input to play game!
            
        if str(gameStart) == 'n':
                currentHand = dealHand(HAND_SIZE)
                oldHand = currentHand.copy()
                # copy current hand to save for replay
                playHand(currentHand, wordList, HAND_SIZE)
                playGameOld(wordList, oldHand)
                # loop to beginning after playHand is over with copied hand
        elif str(gameStart) == 'r':
                if oldHand == '':
                    print('You have not played a hand yet. Please play a new hand first!')
                    playGameOld(wordList, '')
                    # loop back to beginning
                else:
                      playHand(oldHand, wordList, HAND_SIZE)
                      playGameOld(wordList, oldHand) 
        elif str(gameStart) == 'e':
                return
        else:
                print('Invalid Command.')
                playGameOld(wordList, '')
                # loop back to beginning
                
    playGameOld(wordList,'')