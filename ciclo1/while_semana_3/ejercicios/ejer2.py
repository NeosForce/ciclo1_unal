#for anidados 10:30
#FPV7-generar las tablas de multiplicar del 1 al 9
print("Tablas del multiplicar de 1 al 9")
#utiliza dos for anidados
for i in range(1, 9+1):  #for externo, i indica cual tabla voy a generar
  print(i,":", end="") 
  for j in range(1, 9+1): #for interno, por cada valor de i, la j toma los valores de 1 a 9
    prod = i * j  
    print ("\t", prod, end="") #aqui termina el for interno, despues de esta instruccion ingreso al for i por debajo
  print("", end ='\n') # aqui termina el for externo, es un cambio de linea
