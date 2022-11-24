import math

#
# Napište program, který zjistí, zda zadané číslo je prvočíslo

flag = 1
Num = int(input("zadejte cislo: "))
Num_half = math.ceil(Num / 2)

for k in range(2, Num_half + 1):
    if (Num % k) == 0:
        flag = 0
        break

if flag == 0:
    print(Num, " neni prvocislo")
else:
    print(Num, " je prvocislo")
