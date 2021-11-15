# ScriptName: my_functions.py
# Author: Tanmoy Debnath 21324683

# template for calling functions in another file


from typing import List


def print_function():
    print("I'm in another file :)")

#Q1

def seasons(number):

    seasons_list = ["Winter","Spring", "Summer", "Autumn"]

    if type(number) != int:
        return "Input value(s) must be a number"
    
    elif number > 0 and number <= 4:
         return seasons_list[number - 1]

    else:
         print("Number entered," , number, ", is outside of input values")

#Q2

def slice_reverse(input_value):
    '''
    The program returns boolean True or False depending on the input
    '''

    return_value = input_value[::-1]

    if return_value == input_value:
        return True
    	
    else:
        return False

#Q3

def add_to_list(value, list= []):
    
    try:
        if type(list) == type([]):
            if value in list:
                return list 

            elif value not in list:
                list.append(value)
                list.sort()
                return list 

        else:
            return "Incorrect value defined for param list"

    except:
        return "sort() does not like this mixture of elements"

#Q4
def add_to_list_no_sort(value, list=[]):

    i = 0
    list2 =[]

    if type(list) != type([]):
        return "Incorrect value defined for param list"

    try:
        
        if type(value) == str and type(list[0]) == int:
            x = list[0]
            x = str(x)
            ordvalue = ord(value)
            ord0 = ord(x)
            if ordvalue > ord0:
                list.append(value)
            else:
                list.insert(0, value)
            return list
        
        if type(value) == int and type(list[0]) == int:
            if value not in list:
                list.append(value)
                length_of_list = len(list)
                while i < length_of_list:
                    minimum = min(list)
                    list2.append(minimum)
                    list.remove(minimum)
                    i += 1
                return list2

            else:
                return list

        if type(value) == str and type(list[0]) == str:
            if value not in list:
                list.append(value)
                length_of_list = len(list)
                while i < length_of_list:
                    minimum = min(list)
                    list2.append(minimum)
                    list.remove(minimum)
                    i += 1
                return list2

            else: 
                return list

    
        else: 
            value = str(value)
            x = list[0]
            x = str(x)
            ordvalue = ord(value)
            ord0 = ord(x)
            if ordvalue > ord0:
                list.append(value)
            else:
                list.insert(0, value)
            return list

    except:
        list.append(value)
        return list











































    # list2 = []
    

    # if type(list) == int or type(list) == str or type(list) == float:
    #     return "Incorrect value defined for param list"

    # elif type(list) == type([]):
    #     if value in list:
    #         return list 

    #     elif value not in list:
    #         list.append(value)
            
    #         try:
    #             while list:
    #                 min = list[0]
    #                 for var1 in list:
    #                     if var1 < min:
    #                         min = var1
    #                 list2.append(min)
    #                 list.remove(min) 

    #         except:
                
    #             if type(list[0]) == int and value == str:
    #                 list.remove(value)
    #                 return [value] + list
                    
    #             elif type(value) != type(list[0]):
    #                 list.remove(value)
    #                 return list + [value]
         
    # return (list2)
    
    




































    
    # list2 = []

    # i=0
    # x = list[i]
    # x = str(x)
    # y = list[len(list)-1]
    # y = str(y)
    

    # while ord(str(value)) >= ord(x) and ord(str(value)) <= ord(y):
    #     var1 = list[0]
       
    #     var2 = list[1]
      
    #     var3 = list[2]
        
    #     var4 = list[3]
       

    #     if ord(str(var1)) < ord(str(value)):
    #         list.remove(var1)
    #         list2.append(var1)
    #     if not ord(str(var1)) < ord(str(value)):
    #         list2.append(value)
    #     if ord(str(var2)) < ord(str(value)):
    #         list.remove(var2)
    #         list2.append(var2)
    #     if not ord(str(var2)) < ord(str(value)):
    #         list2.append(value)
    #     if ord(str(var3)) < ord(str(value)):
    #         list.remove(var3)
    #         list2.append(var3)
    #     if not ord(str(var3)) < ord(str(value)):
    #         list2.append(value)
    #     if ord(str(var4)) < ord(str(value)):
    #         list.remove(var4)
    #         list2.append(var4)
    #     if not ord(str(var4)) < ord(str(value)):
    #         list2.append(value)

    #     else:
    #         list2.append(value)
    #         list2.append(var1)
    #         list2.append(var2)
    #         list2.append(var3)
    #         list2.append(var4)


    #     return list2 
            
    

    
   

    
    


    
    







    




    

