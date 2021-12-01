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

    # print(while_loop())
    # print(is_stairs ( [1,2,3] ) ) 
    # print(is_stairs ( [1,2,4] ) ) 
    # print(is_stairs ( [3,2,1] ) ) 
    # print(is_stairs ( [3,1,3] ) ) 
    # print(is_stairs ( ["C", "b", "a"] ) ) 
    # print(is_stairs(["c", "b", "a"]))
    # print(is_stairs(["a", "B", "c"]))
    # print(is_stairs(["a", "b", "C"]))
    # print(is_stairs(["c", "B", "a"]))
    # print(is_stairs(["C", "b", "a"]))
    # print(is_stairs ( ["a", "d", "c"] ) ) 
    # print(is_stairs(["a", "b", "c"]))
    # print(is_stairs([2.2,4.4,5.5]))
    # print(while_loop(14))
    print(all_pairs("abc", "abc"))
if __name__ == "__main__":
    ''' call the main() function in this file '''
    main()


