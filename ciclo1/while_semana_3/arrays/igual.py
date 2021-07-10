#determinar si un caracter corresponde un numero o no
#Los numeros corresponden al ord() del 48 al 57 en la tabla ascii
codigo= ord(input("ingrese un solo caracter: "))
print(codigo)
bandera: bool = 48<=codigo<=57
print(bandera)