#dada una cadena, determine si el codigo ascii del 1er caracter de la cadena es par o no
c='bogota'#input("ingrese una cadena: ")
d=ord(c[0])  # ord(char)
print(d)
es_par= d%2 == 0
print(es_par)