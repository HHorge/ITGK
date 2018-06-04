y = 0

a = 0
b = 1

p = 5
q = 6

prodPQ = p * q
produkt = 1

svar = ""
fasit = False

for x in range(101):
    y = x + y
print(y)

while produkt <= 1000:
    a += 1
    produkt *= a

print(produkt)
print(a)

while fasit == False:
     print("Hva er ", p, " * ", q, "?", end="")
     svar = int(input(""))

     if svar == prodPQ:
          fasit = True
          print("Korrekt!")
     else:
          print("Prøv igjen")






