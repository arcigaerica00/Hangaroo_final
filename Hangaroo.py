def isWordGuessed(secretWord, lettersGuessed):
    tester=0
    for letterS in secretWord:
        if letterS in lettersGuessed:
            tester+=1
        else:
                return False
    return True
    
def getAvailableLetters(lettersGuessed):
    list=""
    import string
    availableL=string.ascii_lowercase
    for availL in availableL:
        if availL not in lettersGuessed:
            list= list+ availL
    return (list)

def Hangaroo(secretWord):
    
    import string
    availableL=string.ascii_lowercase
    lettersGuessed = []
    list(lettersGuessed)
    mistakesMade = 0
    secretWord=secretWord.lower()
    
    print("Let's Play Hangaroo!")
    print("The word is " +  str(len(secretWord))  + " letters long.")
    print("You have made",mistakesMade,"mistakes!")
    print(getGuessedWord(secretWord,lettersGuessed))
    
    while mistakesMade < 1000000000:
        if isWordGuessed(secretWord, lettersGuessed):
            return print("Awesome! You got the word right!")
        
        print("Available letters: ")
        print(getAvailableLetters(lettersGuessed))
            
        guess = input("Type a letter to guess the word: ")
        guess = guess.lower()
        
        if guess not in lettersGuessed:
            lettersGuessed.append(guess)
            
            if guess in secretWord:
                print("You got a letter right! Way to go!")
                print(getGuessedWord(secretWord, lettersGuessed))
            else:
                mistakesMade += 1
                print("Nope!Try again!")
                print("You have made",mistakesMade,"mistakes!")
                print(getGuessedWord(secretWord, lettersGuessed))
            
        else:
            print("You already tried that letter!")
            print(getGuessedWord(secretWord, lettersGuessed))
            
    return print("Try Again! You have unlimited tries!")
