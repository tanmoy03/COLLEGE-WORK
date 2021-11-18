# ScriptName: my_functions.py
# Author: Jason Quinlan & Tanmoy Debnath 121324683

# template for calling functions in another file


def print_function():
    print("I'm in another file :)")

# a
def count(my_list, value):
    '''
    function - count how many times <value> occurs in <my_list>
    :param list: - <my_list> input
    :param value: - <value> to search for
    :return:
    '''
    try:
        # set counter
        i = 0
        # accumulator to count how many times <value> occurs
        # set to zero to cover no <value> in <list>
        num_values = 0
        # loop over the length of the <list>
        while i < len(my_list):
            # if <value> and <list> index i are the same
            if my_list[i] == value:
                # increment the accumulator
                num_values += 1
            # increment the counter
            i += 1
        # return how many times <value> occurs in <list>
        return num_values
    except:
        return "Houston, we have a problem!"

# b
def index(my_list, value):
    '''
    function to return the first index that value occurs in my_list
    '''
    try:
        #set counter
        i=0
        # loop over the length of my_list 
        while i < len(my_list):
            # if value in my_list and if the index "i" of my_list is equivalant to value it returns "i" (i.e. the number that value occurs in)
            if value in my_list:
                if my_list[i] == value:
                    return i
                i +=1
            # if value not in my_list it returns -1
            if value not in my_list:
                return -1
    except:
        return "Houston, we have a problem!"

# c 
def get_value(my_list, index):
    '''
    function to return the value that occurs in my_list at index
    ''' 
    
    #set counter
    i = -len(my_list)
    #while loop over length of my_list
    while i < len(my_list):
        #if index is equal to i, then return the index i
        if index == i:
            return my_list[i]
        i += 1
    else:
        return "Houston, we have a problem!"
        

# d 
def insert(my_list, index, value):
    '''
    inserts value into the index specified by the "index" variable input by the user
    '''

    try:
        i = -len(my_list) # set counter
        value == my_list[i] #value is equal to the index of my list


        while i < len(my_list): #while i is less than the length of the list
            if index == -1 and index == i: #if the index is equal to -1 and the index is equal to i
                return my_list[0:i] + value #return the slice until i and join value to it 

            if index == i: #if index is equal to i
                return my_list[0:i] + value + my_list[i+1:len(my_list)] #return the slice of the list with value replacing the index

            i += 1 #increment i

        if i >= len(my_list): 
            return my_list[0:i] + value
    except:
        return "Houston, we have a problem!"

# e 
def value_in_list(my_list, value):
    try:
        i=0 #set counter

        while i < len(my_list): #while i is less than the length of my_list
            if value == my_list[i]: #if value is equivalent to the index i in my_list
                return True

            i += 1 # increment i 
        
        else:
            return False

    except:
        return "Houston, we have a problem!"

# f
def concat(list1, list2):
    '''
    function joins list1 and list 2 and returns them both as a new list
    '''
    try: 

        

        if type(list1) == list and type(list2) == list:     # else if list1 and list2 are lists
            list3 = list1 + list2    # joins both lists together using +
            return list3       # returns a new list called list3

        elif type(list1) == str and type(list2) == str:   # if list1 is a string and list2 is a string
            return (list1 + " " + list2)  # it joins both paramaters together and adds a space between them
        
    
        elif type(list1) == list and type(list1) != type(list2):
            list4 = []
            list4.append(list2)
            list5 = list1 + list4
            return list5

        elif type(list2) == list and type(list1) != type(list2):
            list4 = []
            list4.append(list1)
            list6 = list4 + list2
            return list6


        else: 
            list3 = []     # list3 is an empty list
            list3.append(list1)   #  appends list1 value(s) into list3
            list3.append(list2)   # appends list2 value(s) into list3
            return list3 # returns list3

    except:
        return "Houston, we have a problem!"
#g
def remove(value, my_list):
    '''
    if value is in my_list it removes the value
    '''
    try:
        i=0 #set counter
        
        while i < len(my_list): #while i is less than the length of my_list
            if value in my_list and value == my_list[i]: #if the value is inside of my_list and value is equal to i of my_list
                return my_list[0:i] + my_list[i+1:len(my_list)] #return the slicing of index 0 to i and i+1 to length of my_list
            '''
            through this method I am able to completely remove the value by just skipping over it through slicing
            '''
            i += 1 #increment i 

    except:
        return "Houston, we have a problem!"

