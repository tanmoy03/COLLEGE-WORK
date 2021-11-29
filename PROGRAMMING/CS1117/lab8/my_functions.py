# ScriptName: my_functions.py
# Author: Tanmoy Debnath 121324683



from typing import Type

#Q1
def is_stairs(s):

    try:
        new_list = []

        if s[0] == str(s[0]):
            for i in range(len(s)):
                s[i] = s[i].lower()
                new_list.append(s[i])
                for x in range(len(new_list)-1):
                    if ord(new_list[x+1]) == (ord(new_list[x]) + 1):
                        return True
                    if (ord(new_list[x+1]) + 1) == ord(new_list[x]):
                        return True
                    return False

        elif s[0] == int(s[0]):
            if len(s) == 1:
                return False

            step = s[1] - s[0]

            if step != 1 and step != -1:
                return False

            for i in range(1, len(s)-1):
                if s[i+1] - s[i] != step:
                    return False
            
            return True

    except:
        return "How can I get to the second floor if I do not have a stairs?"


#Q2
def while_loop(max_number = ""):

    try:
        my_list = []
        default_list = [1,2,3,4,5,6,7,8,9,10]
        accum = 0

        if max_number == "":
            return default_list

        i = 1

        if max_number > 0:
            while i <= max_number:
                my_list.append(i)
                accum += i
                i += 1
                if i > 12:
                    break
            my_list.append(accum)

        if max_number < 0:
            while i >= max_number:
                my_list.append(i)
                accum += i
                i -=1
                if i < -12:
                    break
            my_list.append(accum)
        
        return my_list

    except:
        return "Did you break the break or should we continue?"

