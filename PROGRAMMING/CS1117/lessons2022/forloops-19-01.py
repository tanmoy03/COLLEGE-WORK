name = "Tanmoy"

# type 1: get item in an iterable data structure 
for letter in name:
    print (letter + "*")

# type 2: get you an index and youre using the index to get the item
for index in range(len(name)): #6
    print(name[index] + "*")

# type 3: get both, get the item and you get the index
for index, letter in enumerate(name):
    print(index, letter)


fnames = ["Mary", "John"]   
lnames = ["Murphy" "O Sullivan"]

students = [fnames, lnames]

for student in students:
    for firstname in student[0]:
        print(firstname)

shopping = [34, 45, 90, 100]
totalSpend = 0  

for shop in shopping:
    totalSpend += shop