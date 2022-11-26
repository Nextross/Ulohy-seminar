def a(num):
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


def c_1():
    """
    Napište program, který vypočítá faktoriál zadaného čísla
    """
    input_num = int(input("Zadej číslo: "))
    result = 1
    for num in range(1, input_num + 1):
        result *= num

    print(f"Faktoriál je {result}")


def c_2():
    factorial = 1
    number = int(input("zadejte cislo"))
    for k in range(1, number + 1):
        factorial = factorial * k

    print("faktorial csila ", number, " je: ", factorial)


def c_3(num):
    # Řešeno rekurzí
    if num > 1:
        return c_3(num - 1) * num
    else:
        return 1


def e_1(string):
    """
    Definujte funkci která zašifruje vstupní parametr typu string a vrátí nový string,
    kde budou písmenka posunutá o jedničku dle ASCII tabulky
    (např z  ́A ́ se stane B ́ apod.)
    """
    return "".join([chr(ord(i) + 1) for i in string])


def e_2(string):
    new_word = ""

    for letter in string:
        new_word += chr(ord(letter) + 1)

    return new_word
