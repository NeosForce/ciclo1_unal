tupla = (11, 9, -2, 3, 8, 5)
a, b, c = (tupla[i] for i in (1, 3, 5))
print("var1 =", a, ", var2 =", b, ", var3 =", c)
""" var1, var2, var3 = (tupla[i] for i in range(0,6,2))
print("var1 =", var1, ", var2 =", var2, ", var3 =", var3) """