def nb_year(p0, percent, aug, p):
    # your code
    n = 0
    while p0 < p:
        p0 = p0 * (1 + percent/100) + aug
        print (p0)
        n+= 1
    return n