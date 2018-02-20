# -*- coding: utf-8 -*-
"""
Created on Sat Dec  9 15:14:12 2017

@author: Ted
"""

def playGame(wordList):
    """
    code by TJS on 12/9/2017 for edX MITx 6.00.1x pset4.7
    reusing code from pset 4.6 but adding in comp player
    
    Allow the user to play an arbitrary number of hands.
 
    1) Asks the user to input 'n' or 'r' or 'e'.
        * If the user inputs 'e', immediately exit the game.
        * If the user inputs anything that's not 'n', 'r', or 'e', keep asking them again.

    2) Asks the user to input a 'u' or a 'c'.
        * If the user inputs anything that's not 'c' or 'u', keep asking them again.

    3) Switch functionality based on the above choices:
        * If the user inputted 'n', play a new (random) hand.
        * Else, if the user inputted 'r', play the last hand again.
      
        * If the user inputted 'u', let the user play the game
          with the selected hand, using playHand.
        * If the user inputted 'c', let the computer play the 
          game with the selected hand, using compPlayHand.

    4) After the computer or user has played the hand, repeat from step 1

    wordList: list (string)
    """
    
    # creating a subfunction to pass the oldHand through
    def playGameOld(wordList, oldHand):
        """
        script to run through old hand, taken from pset4.6
        
        """
       
        gameStartGood = ('n', 'r', 'e')
        playerTypeGood = ('u', 'c')
        # Tuple of approved user inputs
        
        gameInfo = {'gameStart':'','playerType':''}
        # game details dict
                
        while True:
            gameStart = input('Enter n  to deal a new hand, r to replay the last hand, or e to end game: ')
            if oldHand == '' and gameStart == 'r':
                print('You have not played a hand yet. Please play a new hand first!')
            elif gameStart in gameStartGood:
                break
            else:
                print('Invalid Command.')
        # ask user input to play game, only continue when entered correct letter
        
        if str(gameStart) == 'e':
            return
            # exit game here
            # if user inputs e then immediately exit the game
        
        gameInfo['gameStart'] = gameStart
        # adding the gameStart option into the gameInfo dict
        
        while True:
            playerType = input('Enter u to have yourself play, c to have the computer play: ')
            if playerType in playerTypeGood:
                break
            else:
                print('Invalid Command.')
        # ask user input for who will play game, only continue when entered correct letter
        
        gameSetup = [str(gameStart), str(playerType)]
        
        
        if gameSetup == ['n','u']:
            currentHand = dealHand(HAND_SIZE)
            oldHand = currentHand.copy()
            # copy current hand to save for replay
            playHand(currentHand, wordList, HAND_SIZE)
            playGameOld(wordList, oldHand)
            # loop to beginning after playHand is over with copied hand
        
        elif gameSetup == ['n', 'c']:
            currentHand = dealHand(HAND_SIZE)
            oldHand = currentHand.copy()
            # copy old hand to save for replay
            compPlayHand(currentHand, wordList, HAND_SIZE)
            playGameOld(wordList, oldHand)
        
        elif gameSetup == ['r','u']:
            if oldHand == '':
                print('You have not played a hand yet. Please play a new hand first!')
                playGameOld(wordList, '')
                # loop back to beginning
            else:
                playHand(oldHand, wordList, HAND_SIZE)
                playGameOld(wordList, oldHand)
        
        elif gameSetup == ['r','c']:
            compPlayHand(oldHand, wordList, HAND_SIZE)
            playGameOld(wordList, oldHand)
                
    playGameOld(wordList,'')