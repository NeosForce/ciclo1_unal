#FPV5-calcular 2 ** n, utilizando multiplicaciones sucesivas =2 . 2 . 2 .2 ....n veces
def dosAlaN(n): #n es una var local
  prod=1
  for i in range(1, n+1): # la var i juega el papel de contar iteraciones
    prod*=2  # range () genera la coleccion 1, 2, 3, 4, 5
  return prod
N=7 #es una var global
print('2 elevado a la: ', N,' = ', dosAlaN(N), sep='')