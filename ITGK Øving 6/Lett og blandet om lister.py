def is_six_at_edge(x):

    if x[0] == 6 or x[-1] == 6:
        return True
    else:
        return False

def average(y):
    return round(sum(y)/len(y), 2)

def median(z):
    z.sort()
    midten = int(len(z)/2)
    return z[midten]

my_list = [7, 4, 5, 3, 52]

print(is_six_at_edge(my_list))
print(average(my_list))
my_list.sort()
print(my_list)
print(median(my_list))