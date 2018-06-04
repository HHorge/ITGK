def find_min(liste, minimum = 100000000):
    if liste[0] < minimum:
        minimum = liste[0]
    if len(liste) < 2:
        return minimum
    return find_min(liste[1:], minimum)

print(find_min([4,2,5,123,54,123,1]))