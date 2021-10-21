

def is_it_blue(param1):
    '''
    is_it_blue - \n
    param1 - string - colour
    '''

    if param1 == "blue":
        print(True)
        return "here we go down to the rabbit hole"

    print(False)
    return "wake up. this was all a dream :) "

print(is_it_blue("red"))


val = True

if val == True:
    print("hi")

if val == False:
    print("yo")

if not val == False:
    print("hey")

if val:
    print("bro")

if not val:
    print("nah bro")




a = 20
b = 10

print(a > b)
print(b > a)