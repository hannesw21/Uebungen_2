lst_1 = list(range(0,100, 3))
print(lst_1)
def potenz(par1):
    return par1*par1*par1
lst_2= list(map(potenz, lst_1))
print(lst_2)
