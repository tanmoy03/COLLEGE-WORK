inFile = open("debanks.txt", "r")
outFile = open("song.txt", "w")

# Method 1: using a python file iterator
# lineNo = 1
# for line in inFile:
#     outputLine = str(lineNo) + " - " + str(len(line)) + " - " + line
#     outFile.write(outputLine)
#     lineNo += 1

# Method 2: read lines method - reads one line, includes \n character
# empty string when it reaches the end of the file

# line = inFile.readline()
# lineNo = 1
# while line != "": #as long as you haven't reached the end of the file
#     print(str(lineNo) + ": " + line)
#     line = inFile.readline()
#     lineNo += 1

# Method 3: use the read() method - Reads ENTIRE file as ONE string
entireFile = inFile.read()
lines = entireFile.split("\n") #gives me a back a list of the lines
lineNo = 1

for line in lines:
    print(str(lineNo) + ": " + line)
    lineNo += 1

# ///////// OR //////////

# for line in range(len(lines)):
#     print(str(lineNo) + ": " + lines[lineNo])

# Method 4: readlines() method: gives you back a list of lines
# lines = inFile.readlines()
# lineNo = 1
# for line in lines:
#     print(str(lineNo) + ": " + line)
#     lineNo += 1

inFile.close()
outFile.close()