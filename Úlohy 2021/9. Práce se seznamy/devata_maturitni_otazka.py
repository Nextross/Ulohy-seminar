import random


def a_1():
    """
    Uživatel zadává slova. Uložte tato slova do seznamu. Poté projděte seznam a vypište
    na obrazovku všechna zadaná slova v opačném pořadí.
    """
    word = input("Zadej slovo (ukončeno 0): ")
    word_array = []

    while word != "0":
        word_array.append(word)
        word = input("Zadej slovo (ukončeno 0): ")

    print(*word_array[::-1], sep="\n")


def a_2():
    word = input("Zadej slovo (ukončeno 0): ")
    word_array = []

    while word != "0":
        word_array.append(word)
        word = input("Zadej slovo (ukončeno 0): ")

    for index in range(len(word_array)):
        print(word_array[-index - 1])


def a_3():
    word = input("Zadej slovo (ukončeno 0): ")
    word_array = []

    while word != "0":
        word_array.append(word)
        word = input("Zadej slovo (ukončeno 0): ")

    word_array.reverse()
    print(*word_array, sep="\n")


def b():
    """
    Uložte do seznamu 50 náhodných celých čísel. Poté projděte seznam a vypište na
    obrazovku všechna čísla dělitelná třemi. Vypočítejte, kolik je v seznamu sudých čísel.
    """
    # Zadání neříká z jakého intervalu (zvolil jsem 0 - 100)
    array = [random.randint(0, 100) for _ in range(50)]
    even_nums = 0

    for num in array:
        if num % 3 == 0:
            print(num)
        if num % 2 == 0:
            even_nums += 1

    print(f"V seznamu je {even_nums} sudých čísel")


def c():
    """
    Vytvořte seznam patnácti n-tic náhodných celých čísel
    První položka seznamu bude jedno náhodné celé číslo v rozsahu 1 až 30.
    Druhá položka seznamu bude dvojice náhodných celých čísel v rozsahu 1 až 30.
    Třetí položka seznamu bude trojice náhodných celých čísel v rozsahu 1 až 30.
    Čtvrtá položka seznamu bude čtveřice náhodných celých čísel v rozsahu 1 až 30. atd.
    Patnáctá položka seznamu bude patnáctice náhodných celých čísel v rozsahu 1 až 30

    Následně vytvořenou strukturu vytiskněte na obrazovku v přehledném formátu, nebo
    zapište do textového souboru. Výsledek může vypadat např. takto:
    (1)
    (12, 4)
    (15, 7 , 29)
    (13, 14, 30, 5)
    (23, 24, 3, 28, 19) atd.
    """
    # V jednom list comprehension
    array = [tuple([random.randint(1, 30) for _ in range(i)]) for i in range(1, 16)]
    print(*array, sep="\n")


def c_2():
    # Více rozepsáno to nahoře
    array = []
    for i in range(1, 16):
        array.append(tuple([random.randint(1, 30) for _ in range(i)]))

    print(*array, sep="\n")


def c_3():
    # Ještě více rozepsáno
    array = []
    for i in range(1, 16):
        temp_array = [random.randint(1, 30) for _ in range(i)]
        array.append(tuple(temp_array))

    print(*array, sep="\n")


def d_1():
    """
    Vytvořte seznam 20ti náhodných n-tic celých čísel. Každá n-tice bude mít počet prvků
    n náhodný v rozsahu 2 až 5. Seznam bude tedy obsahovat 30 skupin čísel, z nichž některé
    budou dvojice, některé trojice, některé čtveřice a některé pětice. Následně vytvořenou
    strukturu vytiskněte na obrazovku v přehledném formátu, nebo zapište do textového
    souboru. Výsledek může vypadat např. takto:
    (1, 5, 78)
    (45, 456)
    (125, 7 , 456, 45, 789)
    (123, 145, 458, 458) atd.
    """
    # V zadání si odporuje "seznam 20ti náhodných n-tic" a "seznam bude obsahovat 30 skupin čísel"
    # Stačí změnit číslo ve funkci range(20)
    # Zadání je stejné jako cvičení c, akorát počet prvků n-tice je náhodný
    array = [tuple([random.randint(1, 1000) for _ in range(random.randint(1, 5))]) for _ in range(20)]
    print(*array, sep="\n")


def d_2():
    # Více rozepsáno to nahoře
    array = []
    for i in range(20):
        array.append(tuple([random.randint(1, 30) for _ in range(random.randint(1, 5))]))

    print(*array, sep="\n")


def d_3():
    # Ještě více rozepsáno
    array = []
    for i in range(20):
        temp_array = [random.randint(1, 30) for _ in range(random.randint(1, 5))]
        array.append(tuple(temp_array))

    print(*array, sep="\n")