iterasjoner = 10
resultat = 0

for x in range(iterasjoner):

    x += 1
    print(x, "-gangen:", sep="")

    for n in range(iterasjoner):
        n += 1
        resultat = x*n
        print(resultat)
    print("")


