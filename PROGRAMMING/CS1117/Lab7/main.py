# ScriptName: main.py
# Author: Jason Quinlan

# template for calling functions in another file

# import functions from other files - different options
# from functions import print_function
# import functions - when you use this you need to call the function using 'functions.<function_name>'
# this option imports all functions, using '*'
from my_functions import *


def main():
    """
    Call the functions defined in the functions.py file
    """
    print_function()

    # test count
    # print(count([1, 2, 3, 4, 5, 6, 7, 6, 5, 4, 3, 2, 1], 4))
    # print(count([1, 2, 3, 4, 5, 6, 7, 6, 5, 4, 3, 2, 1], 8))
    # print(count("hello", "l"))
    # print(count("hello", "h"))
    # print(count("hello", "w"))

    # print(index("hello", "o"))
    # print(index("hello", "p"))

    # print(get_value("hello", -4))
    
    # print(insert("hello", -1, "e"))
    # print(insert("hello", -3, "p"))

    # print(value_in_list("hello", "o"))
    # print(value_in_list("hello", "j"))

    print(concat([5,6,7], "a"))
    print(concat("a", [5,6,7]))
    print(concat("hello", "world"))

    # print(remove("l", "hlello"))


if __name__ == "__main__":
    ''' call the main() function in this file '''
    main()
