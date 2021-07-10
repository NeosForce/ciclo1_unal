i=0 #contador de iteraciones
act=1
while  act > 0: #condicion de parada cuando act se trunque a 0
  ant = act
  i+=1 # i es  para prox iteracion
  act=  1 / 2 * ant   #actualizacion 
eps=ant
i=i-1 #ajusto el contador porque me pase una iteracion, en la ultima iteracion act se trunco
print(i, eps)  #respuesta
#------#verificacion---------
eps=1/2**(i) 
truncado=eps/2
print(i+1,' iteraciones valor truncado a: ', truncado)