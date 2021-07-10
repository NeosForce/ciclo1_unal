#W2-Desarrollar un programa que dado un numero entero positivo n
#calcule e imprima (separados por espacios) n/2 si es par o 3*n +1 si es
#impar. El programa debe repetir este proceso con el numero resultado
#de la operacion anterior mientras este sea diferente de 1. Por ejemplo para
#el numero 3 debe imprimir 10 5 16 8 4 2 1.
def seriee(N):
  n=N
  while n != 1:
    if n % 2 == 0: 
      n= n//2
    else: 
      n = 3*n+1
    print(n,end=' ')
  return n
N=5
res=seriee(N)