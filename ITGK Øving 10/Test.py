a = "Jeg sender deg 2000kr snart, i tillegg til de 500 jeg skyldte deg 55"

start = 0
number = False
liste_av_beløp = []
for x in range(len(a)):
    if a[x].isdigit() and not number:
        start = x
        number = True
    if number and not a[x].isdigit():
        number = False
        liste_av_beløp.append(a[start:x])
if number:
    liste_av_beløp.append(a[start:])
print(liste_av_beløp)

myList = [1, 5, 87, 23, 41, 23, 95, 73, 12, 45]
sortert = False

def bubble_sort(myList):
    sortert = False
    while not sortert:
        sortert = True
        for x in range(len(myList)-1):
            if myList[x] > myList[x+1]:
                sortert = False
                myList[x+1], myList[x] = myList[x], myList[x+1]
        return myList
print(myList)

randomString = "5"
print(randomString.isdigit())

randomList = [[1, 4, 2, 4], [12, 54, 23, 1], [23, 53, 2, 3, 1]]
def sort_my_list(list_of_lists):
    for x in range(len(list_of_lists)):
        list_of_lists[x] = bubble_sort(list_of_lists[x])
    ny_liste = []
    for x in list_of_lists:
        ny_liste.append(x)
    ny_liste = bubble_sort(ny_liste)
    ny_liste = set(ny_liste)
    annen_liste = []
    for x in ny_liste:
        for y in list_of_lists:
            if x == sum(y):
                annen_liste.append(x)

    return annen_liste

print(sort_my_list(randomList))
