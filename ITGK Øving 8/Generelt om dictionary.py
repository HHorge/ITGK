myFamily = {}



def addFamilyMember(role, name):
    myFamily.setdefault(role, []).append(name)


addFamilyMember("bror", "Arne")
addFamilyMember("mor", "Anne")
addFamilyMember("bror", "Tor")


print(myFamily)
