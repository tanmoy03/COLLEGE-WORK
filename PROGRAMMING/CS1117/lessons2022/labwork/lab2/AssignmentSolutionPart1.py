# Question 1
inFile = open("dna.txt", "r")

entireFile = inFile.read()
lines = entireFile.split("\n")
lineNo = 0
dna = []

for line in lines:
    if line != "":
        dna.append(line)
        print(str(lineNo) + ": " + str(dna[lineNo]))
        lineNo += 1

inFile.close()

# Question 2: part 1
inFile = open("InflammatoryIBS.csv", "r")
lines = inFile.readlines()

def meanBoutsPerPatient(list):
    values = list.strip("\n")
    values = values.split(",")
    sum_of_values = 0
    for number in values:
        number = int(number)
        sum_of_values += number
    average = sum_of_values/len(values)
    average = round(average)
    return average
    
lineNo = 0
for line in lines:
    lineNo +=1
    print("Patient " + str(lineNo) + " had " + str(meanBoutsPerPatient(line)) + " inflammatory bouts on average")

# Question 2: part 2
def meanBoutsAcrossAllPatients():

    lineNo = 1 
    sum = 0
    for line in lines:
        values = line.strip("\n")
        values = values.split(",")
        sum_of_values = 0
        for number in values:
            number = int(number)
            sum_of_values += number
        average = sum_of_values/len(values)
        print("Patient " + str(lineNo) + " had " + str(round(average)) + " inflammatory bouts on average")
        lineNo += 1
        sum += average
    avg = sum/3
    return "The average number of inflammatory bouts on this trial medication is: " + str(avg)

print(meanBoutsAcrossAllPatients())

inFile.close()