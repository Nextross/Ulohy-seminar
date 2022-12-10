import math


def a():
    """
    Uživatel zadává slova, ukládají se do pole. Zadávání končí zadáním stringu „0“.
    Poté všechna slova uložíte pod sebe do nového prázdného textového souboru.
    """
    word = input("Zadej slovo (ukončeno 0): ")
    word_array = []

    while word != "0":
        word_array.append(word)
        word = input("Zadej slovo (ukončeno 0): ")

    with open("a.txt", "w") as file:
        print(*word_array, sep="\n", file=file)


def b():
    """
    Vytvořte tabulku funkčních hodnot funkce sin(x) pro x z intervalu <0; 2pi> a uložte
    dvojice hodnot pod sebe do textového souboru, dvojici x, sin(x) na jednom řádku oddělte čárkou:
    x sin(x)
    0, 0
    0.4 , 0.0998
    0.5 , 0.1987
    0.6 , 0.2955 atd.
    """
    with open("b.txt", "w") as file:
        print("x", "sin(x)", sep=", ", file=file)

        x = 0
        while x <= 2 * math.pi:
            print(x, math.sin(x), sep=", ", file=file)
            x += 0.01


def c():
    """
    Máte textový soubor, který obsahuje 10 čísel zapsaných pod sebou. (Napište si je
    v nějakém textovém editoru.) Načtěte tato čísla ze souboru do jednorozměrného pole a sečtěte je.
    Načtená čísla a jejich součet vypište na obrazovku.
    """
    with open("c.txt", "r") as file:
        lines = file.readlines()

    array = []
    for line in lines:
        array.append(int(line.removesuffix(r"\n")))

    print(array)
    print(f"Součet čísel je {sum(array)}")
