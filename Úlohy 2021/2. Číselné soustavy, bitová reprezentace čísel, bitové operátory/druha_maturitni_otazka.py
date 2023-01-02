def a():
    """
    Napište program, který převede číslo typu byte do pole osmi celých čísel (s hodnotami 0-1),
    tedy převede jednotlivé bity do osmiprvkového pole bajtů. Například číslo 14 převede tento program
    na pole s hodnotami prvků: [0], [0], [0], [0], [1], [1], [1], [0]
    """
    # Záleží jestli chceme pouze nezáporná osmibitová čísla (0-255) nebo i záporná osmibitová čísla (-127 až 127)
    # Program bere pouze čísla v intervalu 0 až 255
    while True:
        try:
            num = int(input("Zadej celé číslo typu byte: "))
            if not 0 <= num <= 255:  # Pokud je číslo záporné nebo větší než 255, vyhodí program chybu
                raise ValueError
            else:
                byte = (7 * "0" + str(bin(num))[2:])[-8:]  # Převede číslo do binární soustavy, přidá na začátek 7 nul, přebytečné nuly odebere
                break
        except ValueError:  # Zachytí chybu, cyklus začne znovu, dokud uživatel nezadá správné číslo
            print("Zadané číslo je záporné nebo větší než 8 bitů")

    bit_list = [int(bit) for bit in byte]
    print(bit_list)


def b():
    """
    Napište program, kde bude uživatel postupně zadávat celá čísla (typu byte) a program u
    každého čísla invertuje nejvyšší a nejnižší bit (tedy nultý a sedmý), dále potom druhý nejnižší
    (první bit) nastaví vždy na jedničku a druhý nejvyšší (šestý bit) nastaví vždy na nulu. Výsledné
    číslo potom vždy program vypíše na obrazovku. Zadávání skončí uživatel zadáním čísla -1.
    """
    # Záleží jestli chceme pouze nezáporná osmibitová čísla (0-255) nebo i záporná osmibitová čísla (-127 až 127)
    # Program bere pouze čísla v intervalu 0 až 255
    def invert_bytes(byte_array):
        for index, byte in enumerate(byte_array):
            byte_array[index] = list(byte)
            byte_array[index][0], byte_array[index][7] = str(int(not bool(int(byte_array[index][0])))), str(int(not bool(int(byte_array[index][7]))))
            byte_array[index] = "".join(byte_array[index])

        return byte_array

    byte_array = []
    while True:
        try:
            num = int(input("Zadej celé číslo typu byte (ukončeno -1): "))
            if num == -1:
                break
            if 0 <= num <= 255:
                byte = (7 * "0" + str(bin(num))[2:])[-8:]
                byte_array.append(byte)
            else:
                raise ValueError
        except ValueError:
            print("Zadané číslo je záporné nebo větší než 8 bitů")

    print(byte_array)
    print(invert_bytes(byte_array))


def c():
    """
    Napište program, který převede celé číslo (max. 16 bitové) na text, který bude obsahovat
    zápis čísla v šestnáctkové soustavě. Například číslo 268 převede program na text: “1C” apod.
    """
    # Záleží jestli chceme pouze nezáporná 16-bitová čísla (0-255*255-1) nebo i záporná 16-bitová čísla
    # Program bere pouze čísla v intervalu 0 až 256*256-1
    while True:
        try:
            num = int(input("Zadej celé číslo: "))
            if not 0 <= num <= 256*256-1:
                raise ValueError
            else:
                hex_ = hex(num).removeprefix("0x").upper()
                break
        except ValueError:
            print("Zadané číslo je záporné nebo větší než 8 bitů")

    print(hex_)
