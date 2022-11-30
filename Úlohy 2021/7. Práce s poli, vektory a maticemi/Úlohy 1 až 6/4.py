"""c/ Definujte dvourozměrné pole 10 x 10 (typu char) a vyplňte ho náhodnými
písmenky v rozsahu hodnot a..z
Obsah pole poté vypište na obrazovku."""

import string, random
U=[]
abeceda=list(string.ascii_lowercase)
for i in range(0,10):
    Q=[]
    for j in range(0,10):
        Q.append(random.choice(abeceda))
    U.append(Q)
print(U)