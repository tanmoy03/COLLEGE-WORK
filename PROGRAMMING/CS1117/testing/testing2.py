#def add_to_list(value,alist:list=[]) -> list:
#     alist.append(value)
#     return alist

# def add_to_list(value,alist:list=[]) -> list:
#     if alist == None:
#         alist == []
#     alist.append(value)
#     return alist

# print(add_to_list(7))
# print(add_to_list(6,[]))
# print(add_to_list(8))
# print(add_to_list(9))

i = 0
# alist = [5,6,7,8,9]
alist = "hello"
# alist = list(str(123)
while i < len(alist):

    print("index i:", i,"- value:",alist[i], "- ", type(alist[i]))
    
    j=0
    while j < len(alist[i]):

        inner_list = alist[i]
        # print(inner_list)

        print("index j:", j,"- value:",alist[i][j])

        j += 1

    i += 1




