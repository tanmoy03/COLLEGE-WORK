# ScriptName: main.py
# Author: <add your name here>

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

    # print(seasons("hey"))

    # print(slice_reverse([7,7,7])

    # print(add_to_list(4,"hey"))
    
    # print(add_to_list("g", ["a","d","e"]))

    # print(slice_reverse(("r","o","t","a","v","a","t","o","r")))

    # print(add_to_list_no_sort("b", ["a","d","e"]))
    # print(add_to_list_no_sort(5, [1, 2]))
    # print(add_to_list_no_sort(10000, ["a","d","e"]))
    print(add_to_list_no_sort(5, [1,3,7,9,10,11]))
    print(add_to_list_no_sort("c", ["a","b","d","e"]))
    print(add_to_list_no_sort(5, [1,5,7,9]))
    print(add_to_list_no_sort(5, ["a","b","d","e"]) )
    print(add_to_list_no_sort(5, 5))

  



if __name__ == "__main__":
    ''' call the main() functionin this file '''
    main()
