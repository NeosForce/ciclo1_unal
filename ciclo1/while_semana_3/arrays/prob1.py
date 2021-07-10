#Operadores para comparar si dos cadenas son iguales (==)
#orden lexicografico, se comparan de izquierda a derecha uno a uno los caracteres,
#mientras sean iguales. 
# <, <=, >, >=, !=
#En caso que no sean iguales, si el caracter de la primera cadena es menor que el de la segunda a la primer cadena se le
#considera menor, 
#pero si es mayor, a la primer cadena se le considera mayor.
#ca1='rojas'  =>ca1 < ca2
#ca2='rosas'
a = 'Rojas'
#print('Rosas' > a) #
b = "Rojas"
#print(a == b) #True
c = "Ro" + "jas"  #  c guarda en mem ram, el resultado de "Rojas"
#print(a == c) #True
d = "Ro"
e = "jas"
f = d + e # f guarda las direcciones en mem 
#print(a == f) #True
#print(b <'rojas') #True
#El operador 'is' sirve para determinar si dos cadenas referencian al mismo objeto en la mem
#print(a is b) #True
#print(a is c) #True
print(a is f) #False