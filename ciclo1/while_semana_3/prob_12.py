#PF4, 5!  = 1 . 2 . 3 . 4 . 5 =120
def facto(n):
  f=1 #1 es el modulo de la multiplicacion
  for i in range(1, n+1):
    f = f * i 
  return f 
  
N=5
for j in range(1, N+1): 
   print(j, ' factorial: ', facto(j))