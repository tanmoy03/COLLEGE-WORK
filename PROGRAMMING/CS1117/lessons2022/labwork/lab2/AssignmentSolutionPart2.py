inFile = open("InflammatoryIBS.csv", "r")

entireFile = inFile.read()
lines = entireFile.split("\n")
lineNo = 0
dna = []

def meanBoutsPerPatient2():
    lineNo = 1 
    # sum = 0
    list_of_values = []
    for line in lines:
        values = line.strip("\n")
        values = values.split(",")
        sum_of_values = 0
        
        for number in values:
            number = int(number)
            sum_of_values += number
        average = sum_of_values/len(values)
        # print("Patient " + str(lineNo) + " had " + str(round(average)) + " inflammatory bouts on average")
        list_of_values += [[lineNo, average]]
        lineNo += 1
    return list_of_values

print(meanBoutsPerPatient2())

def writeToFile(param):
    file = open("meanBoutsPerPatient2", "w")
    textline = ""

    for list in param:
        textline += ("Patient " + str(list[0]) + "had " + str(list[1]) + "inflammatory bouts in total\n")
    
    file.write(textline)
    
print(writeToFile(meanBoutsPerPatient2()))

inFile.close()