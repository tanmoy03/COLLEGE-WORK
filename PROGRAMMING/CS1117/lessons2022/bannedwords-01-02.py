MASK = "*"

def generate_banned_words():
    # read banned words in from a file bannedWords and return a list of banned words
    inFile = open("bannedWords.txt", "r")

    bannedWords = []
    for word in inFile:
        word = word.strip("\n")
        bannedWords.append(word)

    inFile.close()

def bleeped(word):
    # Return a cleaned version of parameter 'word' with
    # any black-listed word replaced by asterisks. Ignore any
    # non-letters at the beginning or end of 'word'.

def censor_line(line):
    # Return censored version of the text in string parameter
    # 'line' while preserving word breaks and punctuation.  

    words = line.split(" ")
    for wordIndex in range(len(words)):
        words[wordIndex] = bleeped(word[wordIndex])
    
    return " ".join(words)
    

def censor_file(filename):
    # Generate a modified copy of the named text file containing
    # a censored version of the text.

BANNED_WORDS = generate_banned_words()   
print (BANNED_WORDS)
censor_file("someText.txt")