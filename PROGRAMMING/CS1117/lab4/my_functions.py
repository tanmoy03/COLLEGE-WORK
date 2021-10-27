# ScriptName: my_functions.py
# Author: Tanmoy Debnath 121324683

# template for calling functions in another file

import math

from types import TracebackType


def print_function():
    print("I'm in another file :)")

def seperated_input(param1, param2, sepr = "", endr = "\n"):

    '''
    param1 -string value
    param2 -string value
    sepr -sep string value(defaults to “”)
    endr -end string value(defaults to “\n”)
    '''

    print(str.capitalize(param1), sepr, str.capitalize(param2), endr)

def three_numbers(number_1, number_2, number_3):
    '''
    Ask for 3 numbers
    number_1 -int value
    number_2 -int value
    number_3 -int value
    if these numbers are the same return True
    if not return False
    '''
        
    if number_1 == number_2 and number_1 == number_3:
        return True
    else:
        return False
    
    
def seasons(number):
    '''
    number -int value
    Ask for number
        if number between 1-4 return according season
        if number is outside of this domain return an error message
        number - int value
    '''
    if number == 1:
        return "Winter"
    elif number == 2:
        return "Spring"
    elif number == 3:
        return "Summer"
    elif number == 4:
        return "Autumn"
    
    elif type(number) != int:
        return "Input value must be a number"
    else:
        return "Number entered,", number, ", is outside of input values"
        
    



def grades(grade):
    '''
    grade -int value
    Ask for mark out of 100
    Mark inputted correlates to a grade e.g A,D,F
    return this grade
    if mark is not within the 0-100 domain return and "X"
    '''
    if grade >= 85 and grade <= 100:
        return "A"
    elif grade >= 70 and grade <= 84:
        return "B"
    elif grade >= 55 and grade <= 69:
        return "C"
    elif grade >= 40 and grade <= 54:
        return "D"
    elif grade >= 25 and grade <= 39:
        return "E"
    elif grade >= 0 and grade <= 24:
        return "F"

    else:
        grade > 100
        return "X"
    
def equal_numbers(number_1, number_2):
    '''
    number_1 -int value
    number_2 -int value
    Ask for 2 numbers
    if both numbers are equal return the square root of that number
    if the number entered is not an integer, return an error message
    if the numbers do not equal then return the square of both numbers
    '''
    if number_1 == number_2:
        return math.sqrt(number_1) 

    elif type(number_1) != int or type(number_2) != int:
        return "Input value(s) must be a number"
        
    else:
        return number_1**2, number_2**2 