def isWordGuessed(secretWord, lettersGuessed):
    tester=0
    for letterS in secretWord:
        if letterS in lettersGuessed:
            tester+=1
        else:
                return False
    return True