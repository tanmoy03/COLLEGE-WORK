L1 = [5, 8, 1, 9, 7, 3]
'''L1 = [5, 8, 1, 3, 7, 9] n=6
L1 = [5, 7, 1, 3, 8, 9]
L1 = [5, 3, 1, 7, 8, 9]'''

#Function definition
def SelectionSort (l):

	#for loop - number of rounds/iterations over the list we need to take
	for noIterations in range (len(l) - 1):	#generate 5 numbers (0-4 inclusive)
		#what's my largest number in the list? use max()
		largestNo = max(l[0:len(l) - noIterations])			
		#What's the position of this number?
		largestIndex = l.index(largestNo)
		
		#Where am I swapping it to?
		#swap the number at the end of the list to the index where the largest number is
		l[largestIndex] = l[len(l) - (noIterations+1)]
		#swap the largest number to the 'end' of the list (remember the end is decreasing with each round/pass).
		l[len(l) - (noIterations+1)] = largestNo
		
		print(l)		#so that we can see the output after every round/pass/cycle/iteration
		
	return l			#return the fully sorted list

	#Function invocation
myList2 = SelectionSort (L1)