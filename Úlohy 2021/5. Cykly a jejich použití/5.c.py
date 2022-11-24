#
# napište program, který na základě zadaného čísla vypíše pyramidu z hvězdiček:


Row = int(input("zadejte pocet radku: "))
Line = int(input("zadejte delku radku: "))

for k in range(Row):
    for l in range(1, Line + 1):
        print(l, end="")
    print()
