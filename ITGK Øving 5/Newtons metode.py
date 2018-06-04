import math
h, tol = 0.00000001,  0.0000000001
h2, tol2 = 0.00000001, 0.0000000001
h3, tol3 = 0.00001, 0.00001
x = -2
x2 = 1
x3 = -1

def newtonF(x):
    newton = (x-12)*math.e**(5*x)-8*(x+2)**2
    return newton

def newtonG(x):
    newton2 = -x-2*x**2-5*x**3+6*x**4
    return newton2

def derivate(h,x,func):

    deriverte = (func(x + h/2)-func(x-h/2))/h

    return deriverte
def newtons_method(h, x, func, tol):

    while True:
        y = x - func(x)/derivate(h, x, func)

        if y-x <= tol and x-y <= tol: #absoluttverdi
            break
        x = y

    return y, func(y)

#print(newtonG(x))
#print(newtonG(1))

#print(derivate(h, x, newtonF))
print(newtons_method(h, x, newtonF, tol))
print(newtons_method(h2, x2, newtonG, tol2))
print(newtons_method(h3, x3, newtonG, tol3))