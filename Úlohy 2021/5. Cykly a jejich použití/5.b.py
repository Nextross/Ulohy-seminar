#
# uživatel zadá 2 celá čísla. Program vypíše obdélník tohoto typu:
# 1234567
# 1234567
# 1234567
# 1234567

rows = int(input("zadejte pocet radku: "))

for k in range(rows + 1):
    for l in range(k):
        print("*", end="")
    print()
