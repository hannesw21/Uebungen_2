#Mit List Comprehension
lst_1=list(range(1,100))
lst_2=[x*x+x for x in lst_1]
print(lst_1)
print(lst_2)
#Mit Map-Funktion
def rechnung (par1):
    return par1*par1+par1
lst_3= list(range(1,100))
ergebnis = list(map(rechnung, lst_3))
print(lst_3)
print(ergebnis)
