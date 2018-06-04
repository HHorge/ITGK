number_list = []
sum = 0
my_array = list(range(100))


for i in range(100):
    number_list.extend([i])

for n in range(len(number_list)):
    if number_list[n] % 3 == 0 or number_list[n] % 10 == 0:
        sum += number_list[n]

print("Oppgave A og B:")
print(number_list)
print("Summen er: ", sum, sep="")

number_list2 = [] + number_list

for a in range(0, len(number_list), 2):
    number_list[a], number_list[a+1] = number_list2[a+1], number_list2[a]

print("Oppgave C:")
#Fancy map løsning
#print(list(map(lambda x: x+1 if not x%2 else x-1, my_array)))
print(number_list)

#Min første, ikkefungerende løsning
# for b in range(len(number_list)):
#     reversed_list[b] = number_list[-b]
# print(reversed_list)

#Potensiell løsning
# for b in number_list and number_list2:
#     number_list[b] -= 99
#     number_list[b] *= (-1)

reversed_list = [] + number_list[::-1]

print("oppgave D:")
print(reversed_list)

