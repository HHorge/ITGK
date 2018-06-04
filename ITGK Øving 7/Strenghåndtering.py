str1 = "hei"
str2 = "hello"
str3 = "hello"
str4 = "Morna Jens"
str5 = "racecar"
str6 = "pepperkake"
str7 = "per"
str8 = "ola"

#Oppgave A)
def check_equal(string1, string2):
    return string1 == string2

print("oppgave A")
print(check_equal(str1, str2))
print(check_equal(str2, str3))

#Oppgave B)
def reversed_word(str):
    a = ""
    for x in range(1, len(str)+1):
        a += str[-x]
    return a

def reversed_word2(str):
    a = ""
    for char in str:
        a = char + a
    return a
print("\nOppgave B")
print(reversed_word(str4))
print(reversed_word2(str4))

#Oppgave C)

def check_palindrome(str):
    a = ""
    for char in str:
        a = char + a
    return a == str

print("\noppgave C")
print(check_palindrome(str5))

#oppgave D)


def contains_string(str1, str2):
    return str2.find(str1)

#Hjemmelagd funksjon
def contains_string2(str1, str2):
    if str1 in str2:
        for x in range(len(str2)):
            if str1 == str2[x:x+len(str1)]:
                return x
    else:
        return -1

print("\noppgave D")
print(contains_string(str7, str6))
print(contains_string(str8, str6))


print(contains_string2(str7, str6))
print(contains_string2(str8, str6))


