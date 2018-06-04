file = "minfil.txt"
f = open(file, 'w')

def writeToFile(data):

    return f.write(data+"\n")

def readFromFile(filename):
    f = open(filename, "r")
    innhold = f.read()
    print(innhold)



def main():

    userInput = input("Vil du skrive eller lese fil (S/L)?")

    if userInput.upper() == "S":
        userInput = input("Skriv det du vil: ")
        writeToFile(userInput)
        while not userInput.upper() =="DONE":
            writeToFile(userInput)
            userInput = input(">> ")

    f.close()
    userInput = input("Ønsker du nå å lese fra fil?")
    if userInput.upper() == "L" or userInput.upper() == "J":
        fileName = input("Hva heter filen du øsker å åpne?")
        readFromFile(fileName)

    f.close()

main()



