def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    # FILL IN YOUR CODE HERE...
    
    for letter in secretWord:
        if letter not in lettersGuessed:
            return False
    
    return True


def getGuessedWord(secretWord, lettersGuessed):
    
    guessedWord = secretWord
    for letter in guessedWord:
        if letter not in lettersGuessed:
            print(letter)
            guessedWord = guessedWord.replace(letter,"_ ", len(secretWord))

    return guessedWord        


import string
def getAvailableLetters(lettersGuessed):
    
    all_lower = string.ascii_lowercase

    for letter in lettersGuessed:
        if letter in all_lower:
            all_lower = all_lower.replace(letter,'')
    
    return all_lower
