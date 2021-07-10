#El metodo find/rfind() retorna la posicion de la primera/ultima ocurrencia de una
#subcadena en una cadena (o en una parte de ella). 
#Ejemplo: find/rfind(subcadena, inicio, fin)
str2 = 'It is not despair, for despair is ' \
'only for those who see the end ' \
'beyond all doubt. We do not.'
print('primera:', str2.find('despair'))
print('ultima:', str2.rfind('despair'))