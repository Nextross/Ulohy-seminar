"""f/ Definujte jednorozměrné celočíselné pole o 100 prvcích a vyplňte ho náhodnými
reálnými čísly v rozsahu hodnot <-200; 200>.
Vypočítejte součet všech prvků. Najděte největší a nejmenší prvek. (Vypište na
obrazovku.) """

import random, math

L=[]
for i in range(0,100):
    L.append(random.randint(-200,201))

print("součet všech prvků je: ",sum(L))
print("největší číslo je: ", max(L))
print("nejmenší číslo je: ", min(L))
