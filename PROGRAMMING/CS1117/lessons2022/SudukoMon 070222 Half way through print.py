def readBoard (file):
    	
	inFile = open(file, "r")
	b = []

	rows = inFile.readlines()	#list of strings
	for row in rows:
		row = row.strip("\n").split(" ")
		row = [int(num) for num in row]

		b.append(row)

	inFile.close()

	return b

def printBoard (SBoard):
	#//First Hint. You need to print every row. 
	# Think of % (modulus) and you would like to print the dividing sets of characters at the start, 
	# end and after every third row
	#//Second Hint: Within every row you would like to print every column in that row. 
	# The character '|' needs to go at the start, end and after every third column. If there's a zero a space should be printed. 

	horizontalEdge = "+---------+---------+---------+"
	verticalEdge = "|"

	for rowIndex in range (len(SBoard)):
		if rowIndex % 3 == 0:
			print (horizontalEdge)
		for colIndex in range (len(SBoard[0])):
			if colIndex % 3 == 0:
				print (verticalEdge)

		#if a number exists alread in a square just print it.

		#if a zero exists you should print a blank square

	#Note you will need to tinker with this to get it to look as it should - think the end character in the print statement. 
			
def solveBoard (b, row, col):

	result = False
	
	#APPROXIMATE Pseudocode - This is provided as a guide. Further details were given in class. 
	#if: Have I reached row number 9. If I have, I've solved the board return True and return the filled out board. 
	#else (recursive case)
		#if the current square is not equal to a '0' recursively call the function again passing in the next square . Sub question: what is the next row/col?
		#else consider every possible combination of number 
			#is this a validNumber?
				#update the square with the number
				#if recursively calling the function again (next row next col) == true:
					#return true and the board
		#At the end of my loop, set the square back to zero, pass back false and the board

	return result, b

def isValidMove (b, row, col, number):

	valid = True

    # CHECK ROW
    # e.g. imagine I'm the number 7 i.e. number = 7?
    # check the the 9 columns in that row
    # if the number at any given square equal to the vairable number return false

    # CHECK COLUMN

    # CHECK MINI GRID
    # figure out what mini grid you're in. To do this you need to get the starting square e.g. 4 // 3 * 3 = 3 (row) and 1 //3 * 3 = 0 (column)

    # once you have your starting point consider every column in that row, then consider the row and the next i.e.
    # nested for loop, outer loop runs three times (for each row) and the inner loop runs 9 times (for each column)

	
# Main Program
filename = "easyPuzzle.txt"
board = readBoard(filename)
print (board)

print("\nPROBLEM:")
printBoard(board)

result, solvedBoard = solveBoard(board, 0, 0)
if result == False:
    print("Solution does not exist")
else:
    print("\nSOLUTION:")
    printBoard(solvedBoard)