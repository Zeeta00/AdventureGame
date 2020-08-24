def fibb(n):
    if n < 0:
        print("incorrect")
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fibb(n - 1) + fibb(n - 2)


antalTal = int(input("skriv ditt tal: "))
def fibbfunktion(w):
    for x in range(w):

        if fibb(x+1)>=33:
            break
        else:
            return fibb(x+1)
print(fibbfunktion(antalTal))


