""" Una tienda de celulares, va a determinar el modelo estrella, definido como aquel que se vende más veces de forma seguida en un período de una semana. Para el efecto identifican con un número de un solo dígito, a 10 modelos preferidos. En el sistema se registra el número que identifica a los modelos que se ha vendido, y en el orden que ocurren (los números quedan separados por un espacio en blanco).

Su tarea es hacer el programa para el conteo de modelos vendidos, es decir, muestre en un renglón los datos de la entrada, separados por un espacio (cuando un modelo se vende varias veces en forma seguida, se muestra el número del modelo una sola vez) y en el segundo renglón muestre el número de veces seguidas que ocurrieron las ventas de ese modelo. 

input: 4 4 0 4 5 5 5 7
output: 4 0 4 5 7
        2 1 1 3 1
"""



ventas = input("Digite los numeros: ").split() 
ventas = list(map(int, ventas)) 
comparador = 'cualquier cosa'
imprimir1= [] 
imprimir2 = []
for i in ventas:      
        if i == comparador:
                sumador = sumador + 1
                imprimir2[len(imprimir2) - 1] = sumador        
        else:
                imprimir2.append(1)
                imprimir1.append(i)
                sumador = 1
                comparador = i
print(*imprimir1)
print(*imprimir2) 
