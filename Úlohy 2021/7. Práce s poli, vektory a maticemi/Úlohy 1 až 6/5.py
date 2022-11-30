"""d*/ Definujte dvě pole, které budou reprezentovat dvě čtvercové matice A,B typu 7
x7.
Obě matice vyplňte náhodnými čísly v rozsahu hodnot <-10; 10>
Předpokládáme, že čtvercová matice M vznikne vynásobením matic A,B.
Napište funkci se dvěma vstupními parametry R,S. Tato funkce vrátí hodnotu prvku
mRS matice M. (Tedy číslo matice M v R-tém řádku a S-tém sloupečku)
Obě původní matice zde považujte za globální proměnné – nebudou tedy vstupními
parametry funkce. Matici M není třeba pro tento úkol definovat ani počítat."""

import random

A=[]
for i in range(0,7):
    Z=[]
    for j in range(0,7):
        a=random.randint(-10,10)
        Z.append(a)
    A.append(Z)


B=[]
for i in range(0,7):
    Y=[]
    for j in range(0,7):
        Y.append(random.randint(-10,10))
    B.append(Y)

w=int(input("zadejte souřadnici prvku v řádku: "))
e=int(input("zadejte souřadnici prvku ve sloupci: "))

vysledek=0

for i in range(len(B)):
    vysledek=vysledek+A[w][i]*B[i][e]

print("Prvek na vaší pozici má hodnotu: ", vysledek)