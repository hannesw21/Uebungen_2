zahl1 = input("Bitte geben Sie eine gewünschte Zahl ein:")
zahl1 = int(zahl1)
for i in range(zahl1):
    print(i, end="\n")
quadrat = (i+1)*(i+1)
zahl1 += quadrat
print(quadrat)
#Mit Funktion
param1 = input("Geben Sie eine Zahl ein: ")
param1 = int(param1)


def quadrat(par1):
    erg = par1*par1
    return erg


for i in range(param1):
    print(i, quadrat(i))
