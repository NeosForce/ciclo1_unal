#PW1 Imprima el cuadrado del nro que el usr ingresa, mientras que el nro sea no negativo
while True:
  nro=int(input('ingrese nro entero, -1 para terminar: '))
  if nro <0: break
  else:print('cuadrado: ', nro**2)
print('fin')