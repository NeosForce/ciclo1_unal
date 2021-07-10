#El metodo split divide una cadena de acuerdo a 
#un delimitador, dejando las partes separadas en una lista. 
#Ejemplo split(delimitador)
sdate = "01-06-2021"
lista= sdate.split("-")  # diferente de slice - rebanada
print(lista)
print('dia:', lista[0], '- mes:', lista[1], '- agno:', lista[2])