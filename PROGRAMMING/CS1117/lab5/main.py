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
    print(fizz_buzz(6,4,6))
    print(grades("H"))

if __name__ == "__main__":
    ''' call the main() function in this file '''
    main()

var1 = str(73312.13)
index_before = var1.index(".")-1
print(int(var1[index_before]))
print(type(int(var1[index_before])))

