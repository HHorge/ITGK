print("INFO \n Dette programmet besvarer om din utleie av egen bolig er skattepliktig.\n Først trenger vi å vite hvor stor del av boligen du har leid ut.\n Angi dette i prosent, 100 betye hele boligen, 50 betyr halve, \n 20 er mindre del av boligen som f.eks. en hybel.")

rentType = input("Leier du ut egen bolig (E/e), Sekundærbolig (S/s), eller Fritidsbolig (F/f)?")
vacationPurpose = ""
vacationHouses = 0
vacationIncome = 0
vacationLimit = 10000

taxExceeding = 0
taxPrHouse = 0
taxTotal = 0

rentPercent = 0
rentYear = 0
rentLimit = 20000



if rentType == "E" or rentType == "e":
    rentPercent = int(input("Oppgi, i prosent, hvor mye av boligen som ble utleid: "))
    rentYear = int(input("Skriv inn hva du har hatt i leieinntekt: "))

    if rentPercent < 50:
        print("Inntekten er ikke skattepliktig.")
        if rentYear >= rentLimit:
            print("Inntekten er skattepliktig.\nSkattepliktigbeløp er: ", rentYear)

    elif rentYear >= rentLimit:
        print("Inntekten er skattepliktig.\nSkattepliktigbeløp er: ", rentYear)
elif rentType == "S" or rentType == "s":
    print("lol")
elif rentType == "F" or rentType == "f":
    vacationPurpose = input("Skriv inn formålet med fritidboligen(e) (Fritid/Utleie): ")
    vacationHouses = int(input("Skriv inn hvor mange fritidsboliger du leier ut: "))
    vacationIncome = int(input("Skriv inn utleieinntekten pr. fritidsbolig: "))

    if vacationPurpose == "Fritid" or vacationPurpose == "fritid":
        print("")

