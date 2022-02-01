def genererate_banned_words():
    # read banned words in from a file bannedWords and return a list of banned words
    inFile = open("bannedWords.txt", "r")

    bannedWords = []
    for word in inFile:
        word = word.strip("\n")
        bannedWords.append(word)

    inFile.close()
    