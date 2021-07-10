#PV3, RB: 5!  = 1 . 2 . 3 . 4 . 5 =120
def facto(n): #var local
  f=1    #1 es el modulo de la multiplicacion
  for i in range(1, n+1): # lenguaje matematico [1, 10) = [1, 9]
    f *=  i #f = f*i
  return f 
N=5 #N es var global
for j in range(1, N+1): # 1, 2, 3, 4, 5
   print(j, ' factorial: ', facto(j))
print('fin')