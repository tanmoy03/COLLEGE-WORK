# ScriptName: my_functions.py
# Author: <add your name here>

# template for calling functions in another file


def print_function():
    print("I'm in another file :)")

'''
def fizz_buzz(param1):
    param1 == int 
    
    if param1 % 3 ==0 and param1 % 5 == 0:
        return "Fizz Buzz"
    elif param1 % 3 == 0:
        return "Fizz"
    elif param1 % 5 == 0:
        return "Buzz"
    if param1 != int:
        print("Input value(s) must be a statement")
'''
    
def fizz_buzz(param1, divisor_1 = 3, divisor_2 = 5):
    
    if type(param1) != int or type(divisor_1) != int or type(divisor_2) != int:
        try: 
            param1 = int(param1)
            divisor_1 = int(divisor_1)
            divisor_2 = int(divisor_2)
        except:
            return "Input value(s) must be a number"
    if param1 % 3 ==0 and param1 % 5 == 0:
        return "FizzBuzz"
    elif param1 % divisor_1 == 0 and param1 % divisor_2 ==0:
        return "FizzBuzz"
    elif param1 % divisor_1 == 0:
        return "Fizz"
    elif param1 % divisor_2 == 0:
        return "Buzz"
    elif param1 % 3 == 0:
        return "Fizz"
    elif param1 % 5 == 0:
        return "Buzz"
    else:
        return param1
    


def grades(number):
    '''
    grade -int value
    Ask for mark out of 100
    Mark inputted correlates to a grade e.g A,D,F
    return this grade
    if mark is not within the 0-100 domain return and "X"
    '''
    if type(number) != str and type(number) != int:
        return "Input value must be a number or letter"
    

    elif number == "A":
        return "85-100"
    elif number == "B":
        return "70-84"
    elif number == "C":
        return "55-69"
    elif number == "D":
        return "40-54"
    elif number == "E":
        return "25-39"
    elif number == "F":
        return "0-24"
    elif type(number) == str:
        return "The input letter grade is outside the range supported"

    elif number >= 85 and number <= 100:
        return "A"
    elif number >= 70 and number <= 84:
        return "B"
    elif number >= 55 and number <= 69:
        return "C"
    elif number >= 40 and number <= 54:
        return "D"
    elif number >= 25 and number <= 39:
        return "E"
    elif number >= 0 and number <= 24:
        return "F"


    else:
        number > 100
        return "X"
