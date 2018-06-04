def gcd(a,b):
    while b > 0:
        gammel_b = b
        b = a % b
        a = gammel_b
    return a
def reduce_fraction(a,b):
    d = gcd(a, b)
    a /= d
    b /= d
    return a, b
tallA = int(input("Skriv inn et heltall: "))
tallB = int(input("Skriv inn et nytt heltall: "))

print("Største fellesnevner er: ", gcd(tallA, tallB))

a1, b1 = 5, 10
a2, b2 = 4, 2
a3, b3 = 42, 13

#oppgave b)
a = [5, 4, 42]
b = [10, 2, 13]

for x in range(3):
    returnA, returnB = reduce_fraction(a[x], b[x])
    print("For a = ",a[x]," og b = ",b[x], " skriver programmet ut: ", int(returnA),"/",int(returnB), sep="")