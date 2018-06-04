#Oppgave a)
fullpris = 440
minipris = 199
miniprisDager = 14

femtiProsent = fullpris / 2
tjuefemProsent = fullpris * 0.75

alderBarn = 16
alderSenior = 60
alderSvar = 0

miniprisSvar = ""
uniformStudent = ""

dagerTilReise = int(input("Hvor mange dager er det til du skal reise? "))

if dagerTilReise >= miniprisDager:
    print("Du kan få minipris til ", minipris, ",- Disse billettene kan ikke endres/refunderes", sep="")
    svar = input("Ønsker du fortsatt minipris (j/n)")

    if svar == "j" or svar == "J":
        print("Takk for pengene, god reise!")
    elif svar == "n" or svar == "N":
        alderSvar = int(input("Skriv inn alderen din: "))
        if alderSvar < alderBarn:
            print("Prisen på biletten blir: ", femtiProsent, ",-", sep="")
        elif alderSvar >= alderSenior:
            print("Prisen på biletten blir: ", tjuefemProsent, ",-", sep="")
        else:
            uniformStudent = input("Er du student, eller militær personell som kommer til å bruke uniform under reisen (j/n)?")
            if uniformStudent == "j" or uniformStudent == "J":
                print("Prisen på biletten blir: ", tjuefemProsent, ",-", sep="")
            elif uniformStudent == "n" or uniformStudent == "N":
                print("Prisen på biletten blir: ", fullpris, ",-", sep="")

elif dagerTilReise < miniprisDager:
    print("Det er for sent for minipris, men du har kanskje rett på rabatt")
    alderSvar = int(input("Skriv inn alderen din: "))

    if alderSvar < alderBarn:
        print("Prisen på biletten blir: ", femtiProsent, ",-", sep="")
    elif alderSvar >= alderSenior:
        print("Prisen på biletten blir: ", tjuefemProsent, ",-", sep="")
    else:
        uniformStudent = input("Er du student, eller militær personell som kommer til å bruke uniform under reisen (j/n)?")
        if uniformStudent == "j" or uniformStudent == "J":
            print("Prisen på biletten blir: ", tjuefemProsent, ",-", sep="")
        elif uniformStudent == "n" or uniformStudent == "N":
            print("Prisen på biletten blir: ", fullpris, ",-", sep="")
