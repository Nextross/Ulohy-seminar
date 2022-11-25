import math
import random


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


def c_1(num_1, num_2):
    """
    Napište funkci se dvěma vstupními parametry (celá čísla), která vrátí hodnotu true, pokud
    jsou obě vstupní čísla sudá nebo obě lichá. Jinak vrátí hodnotu false
    """
    return (num_1 % 2 == 0 and num_2 % 2 == 0) or (num_1 % 2 != 0 and num_2 % 2 != 0)


def c_2(num_1, num_2):
    both_even = num_1 % 2 == 0 and num_2 % 2 == 0
    both_odd = num_1 % 2 != 0 and num_2 % 2 != 0

    if both_odd or both_even:
        return True
    else:
        return False


def d():
    """
    Příšerka v počítačové hře se na každé křižovatce náhodně rozhodne pro jeden ze 4 směrů.
    Na 10 procent půjde zpět, na 40 procent rovně, na 20 procent doleva a na 30 procent
    doprava. Vygenerujte směr a nastavte správně hodnoty proměnných posun_x, posun_y
    (-1; 0; 1), (tak, aby v následujícím kroku příšerka mohla změnit své souřadnice o tyto kroky.)
    """
    pass


def e():
    """
    Házení falešnou kostkou: Generujte 1000 náhodných hodů falešnou šestistrannou kostkou,
    kde čísla padají s pravděpodobností:
    1: 5 procent
    2: 10 procent
    3: 10 procent
    4: 20 procent
    5: 25 procent
    6: 30 procent
    Čísla vypisujte na obrazovku vedle sebe (oddělené čárkou)
    Program vypočítá a vypíše v závěru, kolikrát z 1000 hodů padla jednička a kolikrát šestka
    """
    count_1 = 0
    count_6 = 0

    for _ in range(1000):
        chance = random.uniform(0, 100)

        if chance <= 5:
            num = 1
            count_1 += 1
        elif 5 < chance <= 15:
            num = 2
        elif 15 < chance <= 25:
            num = 3
        elif 25 < chance <= 45:
            num = 4
        elif 45 < chance <= 70:
            num = 5
        else:
            num = 6
            count_6 += 1

        print(num, end=", ")

    print(f"\n1 padla: {count_1}x\n6 padla: {count_6}x")
