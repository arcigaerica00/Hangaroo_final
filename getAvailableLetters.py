def getAvailableLetters(lettersGuessed):
    import string
    availableL=string.ascii_lowercase
    list=""
    for availL in availableL:
        if availL not in lettersGuessed:
            list= list + availL
    return (list)
    