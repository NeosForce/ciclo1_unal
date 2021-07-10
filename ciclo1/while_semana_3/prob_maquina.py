def min_maquina():
  Xi = 1.0 # Valor inicial
  Xo = Xi # ejecuto el bloque que mas adelante se va a repetir, hay por lo menos una iteracion
  Xi = Xo / 2.0
  i=1
  while(Xi > 0.0):
    i+=1   # i=i+1  numero de terminos de la progresion geometrica, cuya razon es 1/2
    Xo = Xi     #bloque
    Xi = Xo / 2.0 #actualiza la var involucrada en la condicion de parada
  return Xo
print("El minimo numero positivo", end = " ")
print("en esta maquina es:", min_maquina())
# print(i)