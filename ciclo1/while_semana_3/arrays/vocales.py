#determinar si un nro entero corresponde a una vocal minuscula, consultar tabla ASCII
d=int(input("numero entero: ")) # input lee caracteres
if (d == 97 or d==101 or d==105 or d==111 or d==117):
  bandera=True
else:
  bandera=False
print(bandera, ' ', chr (d))