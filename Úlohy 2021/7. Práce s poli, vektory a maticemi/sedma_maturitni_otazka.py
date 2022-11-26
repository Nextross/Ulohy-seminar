import random


def a():
    """
    Definujte dvourozměrné celočíselné pole 20 x 20 a vyplňte ho náhodnými čísly v rozsahu hodnot 0 až 50.
    Zjistěte, kolik je v poli sudých čísel a kolik je v poli čísel dělitelných třemi.
    """
    array = []
    even_nums = 0
    devisible_by_3 = 0

    for row in range(20):
        row = []

        for element in range(20):
            num = random.randint(0, 50)
            row.append(num)
            if num % 2 == 0:
                even_nums += 1
            if num % 3 == 0:
                devisible_by_3 += 1

        array.append(row)
        print(row)

    print(f"Sudých čísel je {even_nums}\nČísel dělitelných třemi je {devisible_by_3}")


def b_1():
    """
    Definujte dvourozměrné celočíselné pole 30 x 30 a vyplňte ho celými náhodnými čísly v rozsahu hodnot 0 až 10.
    Vypočítejte součet všech čísel na hlavní diagonále (pomocí jediného for-cyklu).
    """
    # Vytvoření 2D listu
    array = [[random.randint(0, 10) for _ in range(30)] for _ in range(30)]
    total = 0

    for i in range(len(array)):
        total += array[i][i]

    print(f"Součet prvků na hlavní diagonále je {total}")


def b_2():
    array = []

    # Vytvoření 2D listu
    for i in range(30):
        row = []
        for j in range(30):
            row.append(random.randint(0, 10))
        array.append(row)

    total = 0
    for i in range(len(array)):
        total += array[i][i]

    print(f"Součet prvků na hlavní diagonále je {total}")


def c_1():
    """
    Definujte dvourozměrné pole 10 x 10 (typu char) a vyplňte ho náhodnými písmenky v rozsahu hodnot a..z
    Obsah pole poté vypište na obrazovku.
    """
    array = [[chr(random.randint(97, 122)) for _ in range(10)] for _ in range(10)]
    for row in array:
        print(row)


def c_2():
    array = []

    for i in range(10):
        row = []
        for j in range(10):
            row.append(chr(random.randint(97, 122)))

        array.append(row)
        print(row)


def f():
    """
    Definujte jednorozměrné celočíselné pole o 100 prvcích a vyplňte ho náhodnými
    reálnými čísly v rozsahu hodnot <-200; 200>. Vypočítejte součet všech prvků.
    Najděte největší a nejmenší prvek. (Vypište na obrazovku.)
    """
    # V zadání si odporuje "celočíselné pole" a "vyplňte ho reálnými čísly"
    array = [random.uniform(-200, 200) for _ in range(100)]  # Pro celá čísla random.randint(-200, 200)
    array_sum = sum(array)
    min_num = min(array)
    max_num = max(array)

    print(f"Součet je {array_sum}\nNejvětší prvek je {max_num}\nNejmenší prvek je {min_num}")
