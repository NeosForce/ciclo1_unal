#FPV3-numeros pares
#Imprimir los numeros pares en forma descendente hasta 2 que son
#menores o iguales a un numero natural n >= 2, dado.
n=15
#vs: npp    (numero par prox   14)
if n % 2 !=0: # significa que n es impar; halla en numero impar <= n
  npp = n-1
else:  #n es par
  npp=n #inicialice npp

for i in range(npp, 1, -2):
  print(i, end=' ')