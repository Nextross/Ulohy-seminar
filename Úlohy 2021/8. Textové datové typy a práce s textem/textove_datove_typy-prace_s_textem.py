def a_1():
    """
    Uživatel zadá slovo. Program toto slovo vypíše pozpátku ahoj -> joha
    """
    user_input = input("Zadej slovo: ")
    print(user_input[::-1])


def a_2():
    user_input = input("Zadej slovo: ")
    index = len(user_input) - 1

    for _ in user_input:
        print(user_input[index], end="")
        index -= 1


def b_1():
    """
    Uživatel zadá slovo. Program toto slovo vypíše se zdvojenými písmenky 
    ahoj -> aahhoojj
    """
    user_input = input("Zadej slovo: ")
    print("".join([letter * 2 for letter in user_input]))


def b_2():
    user_input = input("Zadej slovo: ")
    double_letters = ""
    for letter in user_input:
        double_letters += letter * 2

    print(double_letters)


def c_1():
    """
    Uživatel zadá slovo. Program mu slovo zašifruje tak, že každé písmenko posune o 1 dle 
    ASCII (z A udělá B apod.)
    """
    user_input = input("Zadej slovo: ")
    print("".join([chr(ord(i) + 1) for i in user_input]))


def c_2():
    user_input = input("Zadej slovo: ")
    new_word = ""

    for letter in user_input:
        new_word += chr(ord(letter) + 1)

    print(new_word)


def d():
    """
    Uživatel zadá jedno delší slovo. (například Anakonda) 
    Program mu vypíše pyramidu z písmenek tohoto slova
    """
    user_input = input("Zadej slovo: ")
    index = len(user_input)

    for _ in user_input:
        print(user_input[:index])
        index -= 1


def e_1():
    """
    Definujte jednorozměrné pole sedmi stringů. Uživatel zadá 7 slov. 
    Program vypočítá, kolikrát se ve všech slovech vyskytuje písmeno e. 
    Program vypíše slova na obrazovku v opačném pořadí. 
    Program vypíše všechna slova „pozpátku“. 
    """
    word_list = [input("Zadej slovo: ") for _ in range(7)]
    word_list_reversed = word_list[::-1]
    words_reversed_list = [word[::-1] for word in word_list]

    count_e = 0
    for word in word_list:
        count_e += word.count("e")

    print(f"Počet e: {count_e}")
    print("Opačné pořadí:", *word_list_reversed)
    print("Opačná slova:", *words_reversed_list)


def e_2():
    word_list = []

    for i in range(7):
        user_input = input("Zadej slovo: ")
        word_list.append(user_input)

    word_list_reversed = word_list[::-1]
    words_reversed_list = []

    for word in word_list:
        reversed_word = word[::-1]
        words_reversed_list.append(reversed_word)

    count_e = 0
    for word in word_list:
        count_e += word.count("e")

    print(f"Počet e: {count_e}")
    print("Opačné pořadí:", *word_list_reversed)
    print("Opačná slova:", *words_reversed_list)

