""""
def load_data (filename):
    inFile = open(filename, "r")
    entireFile = inFile.readlines()
    Infections = {}
    list1=[]
    for line in entireFile:
        print(line)
        line = line.strip("\n")
        line = line.split(",")
        list1.append(line)
    print(list1)

    for list in list1:
        counter = 0
        for value in list:
            Infections[list[counter]] = value
            counter += 1

    #create a dictionary - let's call it Infections

    #read in the data from the file - How should I read this?

    #get every line of data

        #split it on the comma

        #get the key for the dictionary i.e. the county. remember to get rid of the spaces!

        #now get the value to go with that key i.e. the cimulative infection rates. remeber to get rid of spaces and \n

        #for every cimulative infection get rid of the spaces and \n and convert to an int

        #no create the entry in the dictionary
        #dict[key] = value

    return Infections
"""
def load_data (filename):
    inFile = open(filename, "r")
    entireFile = inFile.readlines()
    Infections = {}
    for line in entireFile:
        line = line.strip("\n")
        line = line.split(",")
        var = line.pop(0)
        new_list = []
        for item in line:
            new_list.append(int(item))
        Infections[var] = new_list
    return Infections


def daily_cases (cumulative):
    newInfections = {}
#     #create a new dictionary called newInfections

#     #for every case in the cumulative dictionary i.e. for every county

#         #for every list of cumulative infection values

#             #if it's the first value recorded, take it as is. Record this in the newInfections dictionary as a new value

#             #else get the current cumulative value
#             #subtract the number from the day before
#             #append it to the county in newInfections

#     #return the newInfections dictionary
    return newInfections

cumulativeInfections = load_data("occurences.txt")
print(cumulativeInfections)
# newInfectionRates = daily_cases(cumulativeInfections)

