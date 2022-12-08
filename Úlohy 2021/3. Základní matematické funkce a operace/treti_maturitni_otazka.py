import math


def a():
    """
    Uložte do pole tabulku funkčních hodnot funkcí y = sin(x), y= sin(2x) a y = sin2(x) v intervalu <0, 2pi>
    Hodnoty zapište na jedné řádce
    """
    chart = [["x", "sin(x)", "sin(2x)", "sin2(x)"]]
    i = 0
    while i <= 2 * math.pi:
        values = [i, math.sin(i), math.sin(2 * i), math.sin(i) ** 2]
        chart.append(values)

        i += 0.01

    with open("a.txt", "w") as chart_file:
        for value in chart:
            # Přidá na každý řádek "rozbalený" seznam hodnot
            chart_file.writelines(" ".join([str(i) for i in value]) + "\n")


def b(num):
    """
    Napište funkci, která vypočítá třetí odmocninu z libovolného reálného čísla,
    pokud programovací jazyk umí počítat pouze třetí odmocniny z nezáporných čísel
    """
    # Python třetí odmocninu neumí, ale třetí odmocninu dokážeme přepsat jako
    # x ** 1/3 (x na 1/3)
    if num >= 0:
        print(num ** (1/3))
    else:
        # Obchází problém s mocninou ze záporného čísla
        print(-((-num) ** (1/3)))


def c():
    """
    Napište program, který pomocí cyklu vypočítá součet prvních 20 členů
    konvergentní číselné řady od 1 do 40: 6/n**2. Vypište potom na obrazovku
    druhou odmocninu z vypočítaného součtu
    """
    # Otázka je poněkud zavádějící, "prvních 2O členů" a "řada od 1 do 40"
    # V obou případech je řešení stejné, akorát se změní počet opakování
    num_sum = 0
    for i in range(1, 21):
        num_sum += 6 / (i ** 2)

    print(math.sqrt(num_sum))


def d(base, power):
    """
    V programovacím jazyku není k dispozici obecná mocnina (např. 3 na sedmou).
    Ale jsou k dispozici funkce ln(x) a exp(x). Napište vlastní funkci se dvěma vstupními
    parametry, která bude vracet číslo a umocněné na číslo b. Použijte Vaši funkci pro výpočet a
    vypsání výsledku 3 ** 7 =
    """
    pass
