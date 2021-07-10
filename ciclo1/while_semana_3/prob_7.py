#sume los 1eros n numeros naturales utilizando while
def sumaW(n): #1, 2, 3, 4, 5, 6, ...n
  s = 0  
  i = 0  
  while(i <= n):
    s += i  # ------variable tipo acumuladora
    i += 1  #-------variable tipo contadora, actualizo
  return s
n=6
print(sumaW(n))
verif= n*(n+1)/2
print('verificacion: ',verif)