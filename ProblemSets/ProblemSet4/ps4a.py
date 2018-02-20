# The 6.00 Word Game

import random
import string

VOWELS = 'aeiou'
CONSONANTS = 'bcdfghjklmnpqrstvwxyz'
HAND_SIZE = 7

SCRABBLE_LETTER_VALUES = {
    'a': 1, 'b': 3, 'c': 3, 'd': 2, 'e': 1, 'f': 4, 'g': 2, 'h': 4, 'i': 1, 'j': 8, 'k': 5, 'l': 1, 'm': 3, 'n': 1, 'o': 1, 'p': 3, 'q': 10, 'r': 1, 's': 1, 't': 1, 'u': 1, 'v': 4, 'w': 4, 'x': 8, 'y': 4, 'z': 10
}

# -----------------------------------
# Helper code
# (you don't need to understand this helper code)

WORDLIST_FILENAME = "words.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # wordList: list of strings
    wordList = []
    for line in inFile:
        wordList.append(line.strip().lower())
    print("  ", len(wordList), "words loaded.")
    return wordList

def getFrequencyDict(sequence):
    """
    Returns a dictionary where the keys are elements of the sequence
    and the values are integer counts, for the number of times that
    an element is repeated in the sequence.

    sequence: string or list
    return: dictionary
    """
    # freqs: dictionary (element_type -> int)
    freq = {}
    for x in sequence:
        freq[x] = freq.get(x,0) + 1
    return freq
	

# (end of helper code)
# -----------------------------------

#
# Problem #1: Scoring a word
#
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


#
# Problem #2: Make sure you understand how this function works and what it does!
#
def displayHand(hand):
    """
    Displays the letters currently in the hand.

    For example:
    >>> displayHand({'a':1, 'x':2, 'l':3, 'e':1})
    Should print out something like:
       a x x l l l e
    The order of the letters is unimportant.

    hand: dictionary (string -> int)
    """
    for letter in hand.keys():
        for j in range(hand[letter]):
             print(letter,end=" ")       # print all on the same line
    print()                             # print an empty line

#
# Problem #2: Make sure you understand how this function works and what it does!
#
def dealHand(n):
    """
    Returns a random hand containing n lowercase letters.
    At least n/3 the letters in the hand should be VOWELS.

    Hands are represented as dictionaries. The keys are
    letters and the values are the number of times the
    particular letter is repeated in that hand.

    n: int >= 0
    returns: dictionary (string -> int)
    """
    hand={}
    numVowels = n // 3
    
    for i in range(numVowels):
        x = VOWELS[random.randrange(0,len(VOWELS))]
        hand[x] = hand.get(x, 0) + 1
        
    for i in range(numVowels, n):    
        x = CONSONANTS[random.randrange(0,len(CONSONANTS))]
        hand[x] = hand.get(x, 0) + 1
        
    return hand

#
# Problem #2: Update a hand by removing letters
#
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


#
# Problem #3: Test word validity
#
def isValidWord(word, hand, wordList):
    """
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
    
    for letter in word:
        if updateHand(hand, word)[letter] < 0:
            return False
        
    return True


#
# Problem #4: Playing a hand
#

def calculateHandlen(hand):
    """ 
    Returns the length (number of letters) in the current hand.
    
    hand: dictionary (string-> int)
    returns: integer
    """
    handCount = 0
    for letter in hand:
        handCount += hand[letter]
    return handCount



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


#
# Problem #5: Playing a game
# 

def playGame(wordList):

    def playGame_old(wordList, oldHand):
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
       
        # game variables
        
        oldHand = ''
        
        gameStatus = 0
        # HAND_SIZE = 7
        # number of letters in hand
        gameStart = input('Enter n  to deal a new hand, r to replay the last hand, or e to end game: ')
        # ask user for input on starting game
        
        # add in while loop to keep cycling to beginning forever
        

        if str(gameStart) == 'n':
                currentHand = dealHand(HAND_SIZE)
                oldHand = currentHand.copy()
                # displayHand(currentHand)
                playHand(currentHand, wordList, HAND_SIZE)
                playGame_old(wordList, '')
                # loop to beginning after playHand is over
        elif str(gameStart) == 'r':
                if oldHand == '':
                    print('You have not played a hand yet. Please play a new hand first!')
                    playGame_old(wordList,'')
                    # loop to beginning
                else:
                      # displayHand(oldHand)
                      playGame_old(wordList, oldHand)
                      # playGame(wordList)
                # pull oldHand, if empty then 
        elif str(gameStart) == 'e':
                return
        else:
                print('Invalid Command.')
                playGame_old(wordList,'')
                # loop back to beginning
        print("Goodbye!")
        return
    playGame_old(wordList, '')
#
# Build data structures used for entire session and play game
#
if __name__ == '__main__':
    wordList = loadWords()
    playGame(wordList)