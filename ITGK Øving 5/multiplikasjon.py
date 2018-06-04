tolerance = 0.01

def product(tol):
    prod = 1
    prodNy = 0
    n = 1
    while prod-prodNy > tol:
        prodNy = prod
        prod *= (1+(1/(n**2)))
        n += 1
        print(prod)
    count = n-1
    return round(prod, 2), count

print(product(tolerance))
