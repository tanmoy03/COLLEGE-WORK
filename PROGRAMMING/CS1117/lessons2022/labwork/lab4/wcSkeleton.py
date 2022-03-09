
def readFile (filename):
    #read the file and return a list of words. 
    inFile = open(filename, "r")
    file = inFile.read()
    file = file.replace("\n", " ")
    words = file.split()
    inFile.close()
    return words


def depunctuate (words):
    punctuation = [",", ".", "!", "?", "-", "'", "—", "…"]
    list = []
    for word in words:
        for punc in punctuation:
            if punc in word:
                word = word.strip(punc)
        list.append(word)   

    return list

    #depunctuate the words and return a cleaned list

def countWords (words):
    wc = {}
    freqs = wc.values()
    max = 0

    for i in words:
        i = i.lower()
        if i in wc:
            wc[i] += 1
        else:
            wc[i] = 1
    
    for thing in freqs:
        if thing > max:
            max = thing
    for word in wc:
        if max == wc[word]:
            answer = word 

    outFile = open("output.txt", "w")
    outFile.write(answer+ ":"+str(max))
    outFile.close()

    #create a dictionary
    #if a word doesn't exist add it as a key with 1 as a value
    #it it does exist add 1 to the current count
        
    #process the dictionary to see which word has the highest count.
    #keep track of the highest word and associated count

    #write this to an output file

#Main Program:

#read in the file to get a list of words (best use a function)
words_text = readFile("books.txt")

#depunctuate the lists of words
words_cleaned = depunctuate(words_text)


#count the words, calculate the max and write to a file
print(countWords(words_cleaned))

# wc = countWords(words_cleaned)
# inverse = [(value, key) for key, value in wc.items()]
# print(max(inverse)[1])
