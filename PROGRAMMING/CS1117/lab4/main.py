# ScriptName: main.py
# Author: Tanmoy Debnath 121324683

# template for calling functions in another file

# import my_functions from other files - different options
# from my_functions import print_function
# import my_functions - when you use this you need to call the function using 'my_functions.<function_name>'
# this option imports all my_functions, using '*'
from my_functions import *


def main():
    """
    Call the functions defined in the functions.py file
    """
    print_function()


if __name__ == "__main__":
    ''' call the main() function in this file '''
    main() 
    
    seperated_input("phineas","ferb", "and", "rock!!!\n")
    seperated_input("doofenshmirtz","incorporated", "Evil", "!!!\n")

    print(three_numbers(1,3,3))

    print(seasons("hey"))

    print(grades(94)) 

    print(grades(64)) 

    print(equal_numbers("a", "b"))