import math

hoyde = float(input("Velg høyden til tetraeden: "))
areal = hoyde*(3/math.sqrt(6))
volum = (math.sqrt(2)*areal**3)/12
overflateAreal = math.sqrt(3)*areal**2


print("Overflatearealet er: ", format(overflateAreal, ".2f"))
#print("Volumet er: ", format(volum, ".2f"))
#print("Arealet er: ", format(areal, ".2f"))

print("Et tetraheder med høyde ", hoyde, " har volum ", format(volum, ".2f"), " og areal ", format(areal, ".2f"), ".", sep="")













