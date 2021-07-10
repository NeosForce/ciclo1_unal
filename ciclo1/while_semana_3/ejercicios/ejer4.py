#funcion seno de x en rads alrededor de 0, utilizando los primeros n terminos Serie de McLaurin
import math
from math import pi 
def seno(x,n):
  acum=0. ; sig=1. 
  for i in range(n+1): #i=0,1,2,3,4,5,6,7,8,9,10
    num=x**(2*i+1)
    den=facto(2*i+1)
    ter=sig*num/den
    acum += ter  #--
    sig=sig*(-1) # 1, -1, 1, -1, 1 , -1 ....
  return acum 
ang= float(input("Seno: Ingrese angulo en grados y punto: "))# angulo en grados, se convierte a radianes
rad=ang*pi/180.
res=seno(rad,10)
print(res)