tallA = 0
tallB = 1
sumAB = 0
sumRekke = 0
k = int(input("Velg antall iterasjoner:"))


for x in range(k):
    #a)
    if x == 0:
        sumAB = 0
    elif x == 1:
        sumAB = 1
    else:
        sumAB = tallA + tallB
        tallA = tallB
        tallB = sumAB

    print(sumAB)
    #b)
    sumRekke += sumAB


print("Det ", k, ". tallet er: ", sumAB, sep="")
print("Summen av rekken er: ", sumRekke, sep="")