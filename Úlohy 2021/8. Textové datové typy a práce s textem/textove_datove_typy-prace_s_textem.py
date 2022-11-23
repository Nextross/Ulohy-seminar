def a():
    """
    Uživatel zadá slovo. Program toto slovo vypíše pozpátku ahoj -> joha
    """
    user_input = input("Zadej slovo: ")
    print(user_input[::-1])


def b():
    """
    Uživatel zadá slovo. Program toto slovo vypíše se zdvojenými písmenky 
    ahoj -> aahhoojj
    """
    user_input = input("Zadej slovo: ")
    print("".join([i * 2 for i in user_input]))


def c():
    """
    Uživatel zadá slovo. Program mu slovo zašifruje tak, že každé písmenko posune o 1 dle 
    ASCII (z A udělá B apod.)
    """
    user_input = input("Zadej slovo: ")
    print("".join([chr(ord(i) + 1) for i in user_input]))

def d():
    """
    Uživatel zadá jedno delší slovo. (například Anakonda) 
    Program mu vypíše pyramidu z písmenek tohoto slova
    """
    user_input = input("Zadej slovo: ")
    lenght = len(user_input)

    for i in user_input:
        print(user_input[:lenght])
        lenght -= 1


def e():
    """
    Definujte jednorozměrné pole sedmi stringů. Uživatel zadá 7 slov. 
    Program vypočítá, kolikrát se ve všech slovech vyskytuje písmeno e. 
    Program vypíše slova na obrazovku v opačném pořadí. 
    Program vypíše všechna slova „pozpátku“. 
    """
    word_array = [input("Zadej slovo: ") for i in range(7)]
    word_array_reversed = word_array[::-1]
    words_reversed_array = [word[::-1] for word in word_array]

    count_e = 0
    for word in word_array:
        count_e += word.count("e")

    print(count_e)
    print(*word_array_reversed)
    print(*words_reversed_array)
