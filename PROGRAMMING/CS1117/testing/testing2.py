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

    print("index:", i,"- value:",alist[i], "- ", type(alist[i]))
    i += 1
