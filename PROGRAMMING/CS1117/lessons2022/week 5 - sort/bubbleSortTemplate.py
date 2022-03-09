L1 = [5, 8, 2, 9, 7, 3]

def BubbleSort (list):
	length_list = len(list)
# 	#loop for every round or iteration over the list that we need to take length_list=20, length_list-1 iterations i.e 19
	for noPasses in range(length_list-1):
# 		#loop for every pair we need to examine - in a single given iteration
		for pairNo in range(length_list-1):
			if list[pairNo] > list[pairNo+1]:  
				# list[pairNo], list[pairNo+1] = list[pairNo+1], list[pairNo]   # a way of swapping  x, y = y,x
				temp = list[pairNo]              # creating a temp variable
				list[pairNo] = list[pairNo+1]       
				list[pairNo+1] = temp
				
			
# 			#if the second number is less than the first number
# 				# be ware of x,y = y,x (works) and the inbuilt swap function. While they work we will do a "traditional" swap 
# 				#swap by creating a temporary third variable. 
		
# 		#if change == False:
# 			#return list
# 		#print the list at the end of the round. 
		print("Round", noPasses + 1, ":", list)

# 	#return the list
	return list

myList = BubbleSort (L1)
print(myList)



def binarySearchI(list,data):
	#Algorithm:
	#1. Keep track of two variables First and Last (index), these are incremented
	#or decremented to limit the part of the 
	#list to be searched.
	first = 0
	last = len(list)-1
	found = False
	while found == False:
		#2. Find the middle element of the list: mid = ( first index + last 
  		# index )//2
		mid = (first + last) // 2          # // floor division rounds it to nearest whole number 
		#3. Compare the middle element with the value to be found. If match 
			#found you're finished.
		if list[mid] == data:         # 12 == 8
			found = True        
			return found
		else:
			#4. Check if the middle element is greater than the value to be 
#            found: 
			if list[mid] > data:    
#5. If yes, the element must lie on the first half of the 
		#list.Update last variable
#updating the last index
				last = mid-1    # last = 5 -1 = 4
			else:
#6. else the element must lie on the second half of the 
#list. Update first variable
#updating the first index
				first = mid + 1
	return found
# print(binarySearchI([2,5,7,8,9,11,14,16],8))
print(binarySearchI([3, 5, 6, 8, 11, 12, 14, 15,20, 17, 18],8))

