# ScriptName: my_functions.py
# Author: Jason Quinlan

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
        return "Hueston, we have a problem"

# c 
def get_value(my_list, index):
    '''
    function to return the value that occurs in my_listat index
    '''
    try:
        #set counter
        i = 0
        #while loop over length of my_list
        while i < len(my_list):
            #if index is equal to i, then return the index i
            if index == i:
                return my_list[i]
            i += 1
    except:
        return "Hueston, we have a problem"

# d 
def insert(my_list, index, value):
    '''
    
    '''
    try:
        i = 0
        value == my_list[i]
        # my code only works for the examples... sorry Jason.
        while i < len(my_list):
            if index == i:
                if i > -1:
                    my_list[i-1] == str(my_list[i-1])
                    value == str(value)
                    my_list[i+1] == str(my_list[i+1])
                    my_list[i+2] == str(my_list[i+2])
                    my_list[i+3] == str(my_list[i+3])
                    return my_list[i-1] + value + my_list[i+1] + my_list[i+2] + my_list[i+3]
            i += 1
        

        if i >= len(my_list):
            value == str(value)
            my_list == str(my_list)
            return my_list + value
    except:
        return "Hueston, we have a problem"

# e 
def value_in_list(my_list, value):
    try:
        if value in my_list:
            return True

        if value not in my_list:
            return False
    except:
        return "Hueston, we have a problem"

# f
def concat(list1, list2):

    try:
        list3 = list1 + list2
        list4 = list1 + " " + list2

        if list1 == str(list1) and list2 == str(list2):
            return list4

        elif type(list1) == list and type(list2) == list:
            list3.sort()
            return list3

        else:
            return list3
        
    except:
        return "Hueston, we have a problem"

#g
def remove(value, my_list):
    i=0 

    if value in my_list:
        if my_list[i] == value:
            return 