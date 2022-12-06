import random
import string


def a_1():
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


def a_2():
    H = []
    sude = 0
    liche = 0
    del_3 = 0

    for i in range(0, 20):
        K = []
        for j in range(0, 20):
            a = random.randint(0, 51)
            K.append(a)
            if a % 2 == 0:
                sude += 1
            else:
                liche += 1
            if a % 3 == 0:
                del_3 += 1

        H.append(K)

    print("Počet sudých čísel je: ", sude)
    print("Počet lichých čísel je: ", liche)
    print("Počet čísel dělitelných 3 je: ", del_3)


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


def b_3():
    T = []

    for i in range(0, 30):
        R = []
        for j in range(0, 30):
            a = random.randint(0, 10)
            R.append(a)
        T.append(R)

    soucet_diagonaly = 0
    for i in range(len(T)):
        soucet_diagonaly = soucet_diagonaly + T[i][i]

    print("Součet diagonály je: ", soucet_diagonaly)


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


def c_3():
    U = []
    abeceda = list(string.ascii_lowercase)
    for i in range(0, 10):
        Q = []
        for j in range(0, 10):
            Q.append(random.choice(abeceda))
        U.append(Q)

    print(U)


def d_1(r, s):
    """
    Definujte dvě pole, které budou reprezentovat dvě čtvercové matice A,B typu 7x7.
    Obě matice vyplňte náhodnými čísly v rozsahu hodnot <-10; 10>
    Předpokládáme, že čtvercová matice M vznikne vynásobením matic A,B.
    Napište funkci se dvěma vstupními parametry R,S. Tato funkce vrátí hodnotu prvku
    mRS matice M. (Tedy číslo matice M v R-tém řádku a S-tém sloupečku)
    Obě původní matice zde považujte za globální proměnné – nebudou tedy vstupními
    parametry funkce. Matici M není třeba pro tento úkol definovat ani počítat.
    """
    matrix_a = [[random.randint(-10, 10) for i in range(3)] for j in range(3)]
    matrix_b = [[random.randint(-10, 10) for i in range(3)] for j in range(3)]

    total = 0
    for i in range(len(matrix_a)):
        # V indexu musí být r - 1, protože se matice číslují od 1, ne od nuly
        # Při zadání posledního řádku/sloupce by nastala chyba (index out of range)
        total += matrix_a[r - 1][i] * matrix_b[i][s - 1]

    print(f"Prvek v {r}. řádku a {s}. sloupci je {total}")


def d_2():
    A = []
    for i in range(0, 7):
        Z = []
        for j in range(0, 7):
            a = random.randint(-10, 10)
            Z.append(a)
        A.append(Z)

    B = []
    for i in range(0, 7):
        Y = []
        for j in range(0, 7):
            Y.append(random.randint(-10, 10))
        B.append(Y)

    w = int(input("zadejte souřadnici prvku v řádku: "))
    e = int(input("zadejte souřadnici prvku ve sloupci: "))

    vysledek = 0

    for i in range(len(B)):
        vysledek = vysledek + A[w - 1][i] * B[i][e - 1]

    print("Prvek na vaší pozici má hodnotu: ", vysledek)


def e_1():
    """
    Definujte dva vektory v dimenzi 12 (12 x 1) a vyplňte oba náhodnými čísly
    v rozsahu hodnot <-3; 3>.
    Vypočítejte skalární součin těchto vektorů pomocí cyklu.
    """
    vector_1 = [random.randint(-3, 3) for _ in range(12)]
    vector_2 = [random.randint(-3, 3) for _ in range(12)]

    product = 0
    for i in range(len(vector_1)):
        product += vector_1[i] * vector_2[i]

    print(f"Skalární součin vektorů je {product}")


def e_2():
    vektor1 = [random.randint(-3, 3) for i in range(0, 13)]
    vektor2 = [random.randint(-3, 3) for i in range(0, 13)]

    vysledny_vektor = 0
    for i in range(len(vektor1)):
        vysledny_vektor = vysledny_vektor + vektor1[i] * vektor2[i]

    print("Skalární součin dvou vektorů je: ", vysledny_vektor)


def f_1():
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


def f_2():
    L = []
    for i in range(0, 100):
        L.append(random.randint(-200, 201))

    print("součet všech prvků je: ", sum(L))
    print("největší číslo je: ", max(L))
    print("nejmenší číslo je: ", min(L))


def g_1():
    """
    Definujte dva vektory v dimenzi 5 (5 x 1 ) a vyplňte oba náhodnými čísly v rozsahu hodnot <0; 10>.
    Správným vynásobením těchto vektorů vnikne čtvercová matice. (někdy toto
    násobení vektorů označujeme jako diadický součin). Vypočítejte položky této matice 5x5.
    """
    vector_1 = [random.randint(0, 10) for _ in range(5)]
    vector_2 = [random.randint(0, 10) for _ in range(5)]

    matrix = []
    for i in vector_1:
        row = []
        for j in vector_2:
            row.append(i * j)
        matrix.append(row)

    for i in matrix:
        print(i)


def g_2():
    vector_1 = [random.randint(0, 10) for _ in range(5)]
    vector_2 = [random.randint(0, 10) for _ in range(5)]
    matrix = [[i * j for j in vector_2] for i in vector_1]

    for i in matrix:
        print(i)
