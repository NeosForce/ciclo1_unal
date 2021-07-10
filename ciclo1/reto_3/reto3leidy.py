

ventas = input("Bienvenido, ingrese las ventas ")
comparar = 0
cventas=0
i=1
modelo=0
j=0
for i in ventas:
    modelo = i
    if comparar == modelo:
           cventas = cventas + 1

    elif comparar !=modelo:
         if cventas > 0:
            print ("modelo", comparar, ", ventas", cventas)
            cventas = 1
    comparar = modelo
print("modelo", comparar, ", ventas", cventas)

