# def concat(list1, list2):
        
#     try:
#         list3 = list1 + list2
#         list4 = list1 + " " + list2

#         if type(list1) == list and type(list2) == list:     # else if list1 and list2 are lists
#             return list1 + list2    # returns a new list called list3
        
#         if list1 == str(list1) and list2 == str(list2):
#             return list4

        

#         else:
#             return list3

#     except:
#         return "Houston, we have a problem!"

# def concat(list1, list2):

#     try:
        
#         if type(list1) == str and type(list2) == str:
#             return list1 + " " + list2

#         else:
#             return list1 + list2
        
#     except:
#         return "Houston, we have a problem"


# print(concat([8,9], [5,6,7]))

# print(concat("hello", "world"))

# print(concat(3.9, 8))


my_list = [1,2,3,4,5]

print(my_list.reverse())