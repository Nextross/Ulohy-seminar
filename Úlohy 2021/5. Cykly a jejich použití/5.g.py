#
# Napište program, který vypíše prvních n členů Fibonacciho posloupnosti (první dva členy posloupnosti mají hodnotu jedna, každý další člen je součtem dvou
# předchozích členů, tedy posloupnost vypadá takto: 1,1,2,3,5,8,13, atd.)


lenght = int(input("zadejte pocet clenu: "))
if lenght==1:
    print("1")
else:
    Num1, Num2 = 1, 1
    print(Num1, ", ", Num2, end="")
    for k in range(lenght -2):
        Num = Num1 + Num2
        Num1, Num2 =Num, Num1
        print(", ", Num, end= "")
