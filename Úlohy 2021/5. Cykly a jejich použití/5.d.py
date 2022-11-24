#
# Napište program, který vypočítá faktoriál zadaného čísla

factorial = 1
Number = int(input("zadejte cislo"))
for k in range(1, Number + 1):
    factorial = factorial * k

print("faktorial csila ", Number, " je: ", factorial)
