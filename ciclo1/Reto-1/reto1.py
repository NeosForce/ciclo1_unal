#Floculante           (entrada)
#cal
#litros de cloro salida
#-4 de cal es el doble de kilos de floculante
#floculante<cal
#5cloro=cal+floculante
#uno=cloro<20 litros
#dos=cloro 20 && 30
#tres=cloro 30 && 50
#cuatro= cloro>50
#---------------------------------------------------------------------------------
#(floculate*2)* +4=cal
#(cal+floculante)/5=cloro

#print(floculante cal litros)
#print(uno dos tres cuatro)
# que hace end= " " ? Poner un espacio al final


import math

ventas = int(input("Digite los numeros"))
print( ventas)

""" floculante = int(input("Bienvenido, digite la cantidad de kilos de floculante "))
cal = (floculante*2) + 4
cloro = math.floor((cal + floculante) / 5)
#print(cal)
#print(cloro)

if cloro < 20:
  dia = "uno"
if cloro >= 20 < 30:
  dia = "dos"
if cloro >= 30 < 50:
  dia = "tres"
if cloro > 50:
  dia = "cuatro"
print(floculante ,cal ,cloro)
print(dia)
 """