#vs: epsilon
#posCondicion: 1+2**-i != 1+2**-(i+1), para i in range(0,10000)
i=1
ant=1
nuevo=1/2
while  nuevo < ant: #condicion de parada cuando nuevo y ant sean iguales, porque se truncaron a un valor=0
  pen=ant
  ant=nuevo
  i+=1 # i es  para prox iteracion
  nuevo= 1 / 2**i   #actualizacion 

print(i-2, pen) #pen tiene la respuesta
#---------------
eps=1/2**(i-2) #verificacion
eps1=eps/2
print(i-1,' epsilon: ', eps1)