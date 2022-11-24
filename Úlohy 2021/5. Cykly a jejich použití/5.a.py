#
# uživatel zadává posloupnost čísel ukončenou číslem nula. napište program, který vypíše jejich součet a součin

Numbers = []
a = int(input("zadejte cislo: "))
b = 1
c = 0

while a != 0:
    Numbers.append(a)
    a = int(input("zadejte dalsi cislo: "))

for k in Numbers:
    b = b * k  # soucin
    c += k  # soucet

print(Numbers)
print("soucin:", b)
print("soucet:", c)
