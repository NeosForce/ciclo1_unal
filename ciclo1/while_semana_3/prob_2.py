#ingresar un simbolo, obtenga el codigo ascii de dicho caracter, lo muestre, pare is es mayuscula
simbolo='a'
#la funcion 'ord' retorna el codigo ascii de un simbolo
codigo= ord(simbolo) # el codigo es un entero entre 0 y 255, donde hay caracteres imprimibles y no imprimibles
while 0 <= codigo <= 64 or 91 <=codigo <=255: #condicion de terminacion
  print(codigo)  # --------------
  simbolo=input('ingrese un simbolo (letra, numero, signo de puntuacion), sale con Mayuscula: ')
  codigo= ord(simbolo)
print('Luego del cuerpo while, termino', simbolo)