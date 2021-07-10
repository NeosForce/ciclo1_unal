#simplificando y eliminando el uso de bandera 
dato = 1
suma = 0 #acumulador5
i=0  #contador
while (dato != 0):
  dato = int(input("Ingrese numero entero o 0 para salir: "))
  suma += dato
  i+=1
i-=1 # fuera del cuerpo del while
promedio=suma/i
print(i,suma,promedio)
print(type(promedio))