#se puede construir un triangulo con 3 lados de cualquier longitud?
#revision bibliografica: los triangulos deben cumplir una propiedad que dice
#la suma de dos lados cualquiera debe ser > que el tercer lado, y 
#que la resta de dos lados cualquiera debe ser < a la longitud del tercer lado

def hayTrian(a,b,c):
  r1: bool = a < b+c
  r2: bool = b < c+a
  r3: bool = c < a+b
  r4: bool = a > abs(b-c)
  r5: bool = b > abs(c-a)
  r6: bool = c > abs(a-b) 
  posC: bool = r1 and r2 and r3 and r4 and r5
  return posC
def tipo(a,b,c,er):
  if er:
    tipo =1*(a!=b and a!=c and b!=c)+ 3*(a==b and a==c) + 2 *((a==b and a!=c)or(b==c and b!=a)or(c==a and c!=b ))
  else:
    tipo=0
  return tipo

a=float(input("lado1: "))
b=float(input("lado2: "))
c=float(input("lado3: "))
preCondicion = hayTrian(a,b,c)

bb = tipo(a,b,c,preCondicion)
print(bb)
if bb==3:
  mensaje="Triangulo es equilatero"
elif bb==2:
  mensaje="Triangulo es isoceles"
elif bb==1:
  mensaje="Triangulo es escaleno"
else:
  mensaje="No hay Triangulo"

print(mensaje)
