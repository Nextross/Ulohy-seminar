#
# Zapište program, který vypočítá součet druhých mocnin celých čísel dělitelných sedmi v rozsahu čísel 200 a 300

Numbers = []
b = 1

for k in range(200, 301):
    if (k % 7) == 0:
        Numbers.append(k**2)

for k in Numbers:
    b = b + k
print(b)