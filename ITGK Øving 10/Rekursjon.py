sum = 0
n = 1
minNumber = -1
myList = [5, 4, 6, 1, 6, 2, 3]

#oppgave a)
def recursiveSum(n):
    global sum
    if n > 0:
        sum += n
        recursiveSum(n-1)
    return sum

print(recursiveSum(5))

#oppgave b)
#Min løsning
# def findSmallestElement(numbers):
#     global n
#     global minNumber
#     if not numbers:
#         return 0
#     if n <= len(numbers):
#         print(len(numbers))
#         if numbers[n] >= numbers[n-1]:
#             print(numbers[n-1])
#             minNumber = numbers[n]
#
#     n += 1
#     findSmallestElement(myList)
#
#     return minNumber

def find_smallest_number(numbers):
    # Hvis listen er redusert til ett element => løsning
    if len(numbers) == 1:
        return numbers
    # Finner ut hvordan listen skal reduseres til neste kall
    if numbers[0] < numbers[1]:
        return find_smallest_number([numbers[0]] + numbers[2:])
    else:
        return find_smallest_number(numbers[1:])
        # return find_smallest_number([numbers[0]] + numbers[2:]) if numbers[0] < numbers[1] else find
        # find_smallest_number(numbers[1:])
#Kortversjon
def smallest_rec_short(input):
    if len(input) == 1:
        return input
    return smallest_rec_short([input[0]] + input[2:]) if input[0] < input[1] else smallest_rec_short(input[1:])


print(smallest_rec_short(myList))

print(find_smallest_number(myList)[0])

def findSmallestElement2(numbers):
    if len(numbers) == 1:
        return numbers[0]
    else:
        return min(numbers[0],findSmallestElement2(numbers[1:]))



print(findSmallestElement2(myList))



def binarySearch(numbers, element):



    binarySearch()