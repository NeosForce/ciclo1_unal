#FPV6-Implementar la funcion potencia sin utilizar el operador **, ni la funcion logaritmo 
#v entrada: x, n
#v salida: p
#p= x**n
# p = x . x . x .....x (n veces) -------Hay 3 casos 1) n>0;  2) n =0;  3) n<0
#pero si n es == 0  ... que significa?

# en general p = x**m / x**k =  x**(m-k)  
# 1)si (m - k) == 0 , =>   p= x**m / x**k = 1     => x**0=1
# 2) si (m - k) > 0, p=x**(m-k) = x . x . x . x ... (m-k) veces
# 3) si (m - k) < 0,  p= 1 / x **(|m-k|) => p = 1/ (x . x . x. ...(k-m) veces)
x = 3
def pote(x,n): #x E Reales, n E enteros
  if n==0: # 1er caso
    p= 1
  elif n>0: #caso2 p= x . x. x. ... n veces
    p=1      # en 1 por ser el modulo de la multiplicacion
    for i in range(1, n+1): #i =(1, 2, 3, 4, ... n)
      p *=x #p= p*x, p= 1.x, x.x, x.x.x, x.x.x.x, x.x.x.x.x
  else: # caso n <0   p=1/(x .x . x ... n veces)
    p=1
    for i in range(1, -n+1): #(1, 2, 3, 4)
      p *= x         # x .x . x ... n veces
    p = 1/p
  return p
y=3.; m=-3
res=pote(y,m) #param actuales, coincidan
print(pote(x,m))

#toca pensar que es


