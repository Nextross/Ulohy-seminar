import math


def a():
    """
    Napište program, který vypíše vzestupně všechna celá čísla v rozsahu 1 až 1000, která jsou
    dělitelná 3, nebo 7, nebo 11, ale zároveň nejsou dělitelná osmi.
    """
    values = [i for i in range(1, 1001) if (i % 3 == 0 or i % 7 == 0 or i % 11 == 0) and i % 8 != 0]
    values.sort(reverse=True)

    for i in values:
        print(i)


def b():
    """
    Napište program, kde uživatel zadá koeficienty a,b,c kvadratické rovnice a program na
    základě hodnoty diskriminantu napíše, kolik má rovnice řešení a uvede příslušné (nebo
    příslušná) řešení
    """
    a = int(input("Zadej a: "))
    b = int(input("Zadej b: "))
    c = int(input("Zadej c: "))
    diskriminant = b ** 2 - 4 * a * c

    if diskriminant < 0:
        print("Rovnice nemá řešení")
    elif diskriminant == 0:
        print(f"Řešením je {-b/(2 * a)}")
    else:
        print(f"Řešením je {(-b + math.sqrt(diskriminant))/ (2 * a)} a {(-b - math.sqrt(diskriminant))/ (2 * a)}")
