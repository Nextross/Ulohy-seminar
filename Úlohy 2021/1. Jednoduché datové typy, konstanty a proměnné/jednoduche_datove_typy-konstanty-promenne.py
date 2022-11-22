import math
import random


def a_1():
    """
    Napište program, který vytiskne všechna písmenka od “a“ až do “z“ na obrazovku pod
    sebe pomocí jednoho for-cyklu a jediné proměnné typu char.
    """
    # Python nemá datový typ "char"
    for unicode_code in range(97, 123):
        print(chr(unicode_code))


def a_2():
    # List může být nadefinovaný i ručně, písmeno po písmenu
    letters = [chr(i) for i in range(97, 123)]
    for letter in letters:
        print(letter)


def b():
    """
    Nadefinujte tři proměnné a, b, c typu integer. Vložte do nich náhodné hodnoty v rozsahu 1 až 50.
    Určete jejich průměr. Vypište je od nejvyššího čísla do nejnižšího. Zaměňte hodnoty v
    proměnných a , b.
    """
    a = random.randint(0, 50)
    b = random.randint(0, 50)
    c = random.randint(0, 50)

    values = [a, b, c]
    values.sort()
    
    print(f"a: {a}, b: {b}")
    a, b = b, a
    print(f"a: {a}, b: {b}")
    
    print(f"Průměr je: {(a + b + c) / 3}\nČísla od nejvyššího: {values}")


def c():
    """
    Uživatel zadává celá čísla, zadávání se ukončí nulou.
    Program vypíše součet zadaných sudých čísel a součet zadaných čísel, která jsou dělitelná třemi.
    """
    user_input = int(input())
    sum_odd = 0
    sum_divisible_3 = 0

    while user_input != 0:
        if user_input % 2 == 0:
            sum_odd += user_input
        # Druhý if nemůže být elif, protože kdyby bylo zadané číslo např. 6, tak je první podmínka
        # splněna a druhá se už nespustí
        if user_input % 3 == 0:
            sum_divisible_3 += user_input

        user_input = int(input())

    print(f"Součet sudých čísel: {sum_odd}\nSoučet čísel dělitelných 3: {sum_divisible_3}")


def d():
    """
    Definujte proměnnou “Nahoru”, která bude logického typu. Nastavte ji náhodně tak,
    aby na 30 procent měla pravdivou hodnotu a na 70 nepravdivou hodnotu.
    """
    if random.random() > 0.3:
        nahoru = False
    else:
        nahoru = True

    print(nahoru)
