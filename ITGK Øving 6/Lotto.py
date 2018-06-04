import random

numbers = list(range(1,35))
myGuess = [4, 7, 15, 33, 17, 29, 19]
lottoNum = 7
antallTilleggstall = 3
tilleggstall = []
result = []
myGuess.sort()

def compList(guess, result):
    result.sort()
    guess.sort()
    correct = 0
    for a in range(len(guess)):
        for i in range(len(result)):
            if guess[a] == result[i]:
                correct += 1
    return correct

    #returnerer hvilke tall som er like
    #return set(guess).intersection(result)


def lottoNumbers(num):
    lottoResult = []
    for x in range(num):
    #Lager lottorekke ved å velge "num" tall fra "numbers" og setter de i en ny "lottoresult"-array
        lottoResult.append(numbers.pop(random.randint(0, len(numbers) - 1)))
    return lottoResult


#Tilfeldige hovedtall
lottoResult = lottoNumbers(lottoNum)
#Tilfeldige tilleggstall
tilleggResult = lottoNumbers(antallTilleggstall)

#Sammenligner lottotallene og tilleggstallene med "myGuess"
correctHoved = compList(myGuess, lottoResult)
correctTillegg = compList(myGuess, tilleggResult)

print("Du har ", correctHoved, " riktig(e) hovedtall, og ", correctTillegg," riktig(e) tilleggstall.", sep="")

#Setter sammen hoved og tilleggstallene
result = lottoResult + tilleggResult

print("Din lottorekke:\n", myGuess)
print("Lottorekke med tilleggstall:\n", result)

