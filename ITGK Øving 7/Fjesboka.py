facebook = []
user = ""
global done

def add_data(user):
    user = user.split()
    user[2] = int(user[2])

    return user

def get_person(given_name, facebook):
    a = []
    for x in range(len(facebook)):
        if given_name == facebook[x][0]:
            a.append(facebook[x])
    return a



def main():
    done = False
    fornavn = ""
    while not done:
        print("Legg til bruker på formen\nfornavn etternavn alder kjønn sivilstand")
        user = input("> ")

        if user.upper() == "DONE":
            done = True
        else:
            facebook.append(add_data(user))
    done = False

    while not done:

        fornavn = input("Skriv inn fornavn til bruker du ønsker å finne: ")
        if fornavn.upper() == "DONE":
            done = True
        else:
            print(get_person(fornavn, facebook))

main()
