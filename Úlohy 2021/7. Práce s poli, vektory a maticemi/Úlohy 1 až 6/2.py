import random

"""a/ Definujte dvourozměrné celočíselné pole 20 x 20 a vyplňte ho náhodnými čísly
v rozsahu hodnot 0 až 50.
Zjistěte, kolik je v poli sudých čísel a kolik je v poli čísel dělitelných třemi. 
"""
print("-"*352)
H=[]
sude=0
liche=0
del_3=0
for i in range(0,20):
    K=[]
    for j in range(0,20):
        a=random.randint(0,51)
        K.append(a)
        if a%2==0:
            sude+=1
        else:
            liche+=1
        if a%3==0:
            del_3+=1

    H.append(K)

#print(H)
print("Počet sudých čísel je: ",sude)
print("Počet lichých čísel je: ",liche)
print("Počet čísel dělitelných 3 je: ", del_3)