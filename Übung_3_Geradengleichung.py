a = input("Bitte geben Sie eine Zahl ein:")
a = int(a)
b = input("Bitte geben Sie eine weitere Zahl ein:")
b = int(b)
lst_1 = list(range(-20,+20))
lst_2 = [a*x+b for x in lst_1]
print(lst_1)
print(lst_2)
