tallA = int(input("Skriv inn et heltall: "))
tallB = int(input("Skriv inn et nytt heltall: "))
tallX = 3
tallY = 4

#Oppgave a)
sumAB = tallA + tallB
produktAB = tallA * tallB
produktXY = tallX * tallY

if sumAB < produktAB:
    print(sumAB)
elif sumAB > produktAB:
    print(produktAB)
elif sumAB == produktAB:
    print("Summen og produktet er det samme.")

#Oppgave b)
print("Hva er ",tallX,"*",tallY,"? ", end="")
inputProdukt = int(input("Svar: "))
if inputProdukt == produktXY:
    print("Det stemmer!")
else:
    print("Svaret er dessverre feil.")

