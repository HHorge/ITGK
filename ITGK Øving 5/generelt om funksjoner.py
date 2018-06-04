#oppgave a)
tallX = int(input("Skriv inn et tall:"))
tallY = int(input("Skriv inn et tall du vil gange med det forrige:"))

def ganging(x, y):

    return x*y

print("Produktet av tallene er: ", ganging(tallX, tallY), sep="")

#oppgave b)
def printing(x):
    print(x)
    return

svar = input("Skriv det du vil printe?")
printing(svar)

#oppgave c)
def talletTo():
    return 2

print(talletTo())