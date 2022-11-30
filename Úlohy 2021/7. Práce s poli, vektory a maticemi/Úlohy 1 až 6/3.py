import random

"""b/ Definujte dvourozměrné celočíselné pole 30 x 30 a vyplňte ho celými náhodnými
čísly v rozsahu hodnot 0 až 10.
Vypočítejte součet všech čísel na hlavní diagonále (pomocí jediného for-cyklu). """

T=[]
for i in range(0,30):
    R=[]
    for j in range(0,30):
        a=random.randint(0,10)
        R.append(a)
    T.append(R)


soucet_diagonaly=0
for i in range(len(T)):
    soucet_diagonaly= soucet_diagonaly +T[i][i]

print("Součet diagonály je: ", soucet_diagonaly)
