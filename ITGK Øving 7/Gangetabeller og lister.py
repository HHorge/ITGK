numA = 7
myArray = [1, 4, 5, 11, 7, 34, 65, 1, 33, 66]
numB = 6

def seperate(numbers, threshold):
    smallerThanT = []
    biggerThanT = []

    for i in range(len(numbers)):
        if numbers[i] < threshold:
            smallerThanT.append(numbers[i])
        elif numbers[i] >= threshold:
            biggerThanT.append(numbers[i])
    return smallerThanT, biggerThanT

print(seperate(myArray, numA))


def multiplication_table(n):

    table = [[0 for col in range(n)]
                for row in range(n)]

    for i in range(n):
        for x in range(n):
            table[i][x] = ((x+1)*(i+1))
        print(table[i])


multiplication_table(numB)

# Mapping
num = 5
print([list(map(lambda z: z*x, range(1, num+1))) for x in range(1,num+1)])
