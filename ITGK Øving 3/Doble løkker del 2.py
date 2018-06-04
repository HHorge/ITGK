for x in range(1, 101):

    prime = True

    for i in range(2, x):
        if x % i == 0:
            prime = False
    if prime:
        print(x)


#Proffløsning
for num in range(1, 101):
    if all(num % i != 0 for i in range(2, num)):
        print(num)

