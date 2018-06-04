n = 4
r = 0.5
a = 0
sum = 0
tol = 0.001
grense = 2

#a)
while a <= n:
    sum += r**a
    a += 1

print("Summen av rekken er: ", sum, sep="")
#b) og c)
while sum <= grense-tol:
    sum += r**a
    a += 1

print("For å være innenfor toleransegrensen: ", tol, ", kjørte løkken ", a, " ganger.", sep="")
print("Differansen mellom virkelig og estimert verdi var: ", grense - sum, sep="")

