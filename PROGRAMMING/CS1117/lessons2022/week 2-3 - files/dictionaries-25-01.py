
eircodeAreas = {'A63': 'Greystones', 'A98':'Bray', 'P17':'Kinsale', 
'A86':'Dunboyne', 'W23':'Cellbridge', 
'F45':'Castlerea', 'F35':'Ballyhaunis', 'H14':'Belturbet', 'N39':'Longford', 
'F56':'Ballymote'}


def generateEircodeAreas (filename):
    # IGNORE THIS FUNCTION AS WE HAVEN@T COVERED FILES - DICTIONARY HARD CODED ABOVE
    #connect to the file
    #read the contents from the file (into a list) and generate the dictionary. 
    return eircodeAreas


def getTownLand(eircode):
    #get the routing key from the eircode e.g. A63F4E2
    routingkey = eircode[0:3]
    #use this routing key as a key into the dictionary to get the value i.e. the townland
    townland = eircodeAreas[routingkey]
    return townland


def checkLegitEirCode(eircode):
    legitimate = True
    #check the length of the eircode (7 characters)
    if len(eircode) != 7:
        legitimate = False 
        print("Eircode was not the correct number of characters")
        return legitimate
    #check if the first character of the routing key is a letter
    if eircode[0].isalpha() == False: #asking if string is an alphabetical letter ".isalpha"
        legitimate = False
        print("The first character is not a letter")
        return legitimate
    #check if the 2nd and 3rd characters of the routing are numbers
    if eircode[1].isnumeric() == False or eircode[2].isnumeric() == False:
        print("Second and third character invalid")
        return legitimate
        
    return legitimate


# eircodeAreas = generateEircodeAreas ("eircodes.txt")          
userEirCode = input("Please enter your eircode: ")
legit = checkLegitEirCode(userEirCode)
if legit:
    area = getTownLand(userEirCode)
    print ("You live in: ", area)

