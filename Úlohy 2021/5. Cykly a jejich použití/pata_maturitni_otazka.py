import math


def a_1():
    """
    Uživatel zadává posloupnost čísel ukončenou číslem nula
    Napište program, který vypíše jejich součet a součin
    """
    num = int(input("Zadej číslo: "))
    num_sum = 0
    num_product = 1

    while num != 0:
        num_sum += num
        num_product *= num

        num = int(input("Zadej číslo: "))

    print(f"Součet je {num_sum}\nSoučin je {num_product}")


def a_2():
    numbers = []
    a = int(input("zadejte cislo: "))
    b = 1
    c = 0

    while a != 0:
        numbers.append(a)
        a = int(input("zadejte dalsi cislo: "))

    for k in numbers:
        b = b * k  # soucin
        c += k  # soucet

    print(numbers)
    print("soucin:", b)
    print("soucet:", c)


def b_1():
    """
    Uživatel zadá 2 celá čísla. Program vypíše obdélník tohoto typu:
    1234567
    1234567
    1234567
    1234567 (v případě, že uživatel zadal 4,7)
    """
    height = int(input("Zadej výšku: "))
    width = int(input("Zadej šířku: "))

    for line in range(height):
        for element in range(1, width + 1):
            print(element, end="")

        print("")


def b_2():
    row = int(input("zadejte pocet radku: "))
    line = int(input("zadejte delku radku: "))

    for k in range(row):
        for l in range(1, line + 1):
            print(l, end="")
        print()


def c_1():
    """
    Napište program, který na základě zadaného čísla vypíše pyramidu z hvězdiček:
    *
    **
    ***
    ****
    ***** (v případě, že uživatel zadal číslo 5)
    """
    rows = int(input("Zadej počet *: "))

    for num_of_stars in range(1, rows + 1):
        print('*' * num_of_stars)


def c_2():
    rows = int(input("zadejte pocet radku: "))

    for k in range(rows + 1):
        for l in range(k):
            print("*", end="")
        print()


def d_1():
    """
    Napište program, který vypočítá faktoriál zadaného čísla
    """
    input_num = int(input("Zadej číslo: "))
    result = 1
    for num in range(1, input_num + 1):
        result *= num

    print(f"Faktoriál je {result}")


def d_2():
    factorial = 1
    number = int(input("zadejte cislo"))
    for k in range(1, number + 1):
        factorial = factorial * k

    print("faktorial csila ", number, " je: ", factorial)


def d_3(num):
    # Řešeno rekurzí
    if num > 1:
        return d_3(num - 1) * num
    else:
        return 1


def e_1():
    """
    Napište program, který zjistí, zda zadané číslo je prvočíslo
    """
    input_num = int(input("Zadej číslo: "))
    is_prime = True

    # Prvnočísla jsou pouze přirozená čísla > 1
    if input_num > 1:
        for num in range(2, input_num):
            if input_num % num == 0:
                is_prime = False
                break
    else:
        is_prime = False

    if is_prime:
        print(f"Číslo {input_num} je prvočíslo")
    else:
        print(f"Číslo {input_num} není prvočíslo")


def e_2():
    flag = 1
    num = int(input("zadejte cislo: "))
    num_half = math.ceil(num / 2)

    for k in range(2, num_half + 1):
        if (num % k) == 0:
            flag = 0
            break

    if flag == 0:
        print(num, " neni prvocislo")
    else:
        print(num, " je prvocislo")


def f_1():
    """
    Zapište program, který vypočítá součet druhých mocnin celých čísel dělitelných
    sedmi v rozsahu čísel 200 a 300
    """
    total = 0

    for num in range(200, 301):
        if num % 7 == 0:
            print(num)
            total += num ** 2

    print(total)


def f_2():
    numbers = []
    b = 1

    for k in range(200, 301):
        if (k % 7) == 0:
            numbers.append(k ** 2)

    for k in numbers:
        b = b + k
    print(b)


def g_1():
    """
    Napište program, který vypíše prvních n členů Fibonacciho posloupnosti
    (první dva členy posloupnosti mají hodnotu jedna, každý další člen je součtem dvou
    předchozích členů, tedy posloupnost vypadá takto: 1,1,2,3,5,8,13, atd.)
    """
    lenght = int(input("Zadej číslo: "))
    total = 1
    prev_num = 0
    start_num = 1

    for i in range(lenght):
        print(total, end=", ")
        total = prev_num + start_num
        start_num, prev_num = total, start_num


def g_2():
    lenght = int(input("zadejte pocet clenu: "))
    if lenght == 1:
        print("1")
    else:
        num1, num2 = 1, 1
        print(num1, ", ", num2, end="")
        for k in range(lenght - 2):
            num = num1 + num2
            num1, num2 = num, num1
            print(", ", num, end="")
