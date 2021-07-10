def sumaF(n):  #1,2,3,4,5,6
  s = 0
  for i in range(1, n + 1): # coleccion: range(1, n + 1)
    s += i
  return s
n=6
print(sumaF(n))