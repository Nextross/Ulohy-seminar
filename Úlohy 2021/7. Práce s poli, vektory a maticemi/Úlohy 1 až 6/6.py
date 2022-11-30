"""e*/ Definujte dva vektory v dimenzi 12 (12 x 1 ) a vyplňte oba náhodnými čísly
v rozsahu hodnot <-3; 3>.
Vypočítejte skalární součin těchto vektorů pomocí cyklu. 
"""

import random


vektor1=[random.randint(-3,3) for i in range(0,13)]
vektor2=[random.randint(-3,3) for i in range(0,13)]

vysledny_vektor=0
for i in range(len(vektor1)):
    vysledny_vektor= vysledny_vektor + vektor1[i]*vektor2[i]

print("Skalární součin dvou vektorů je: ", vysledny_vektor)
