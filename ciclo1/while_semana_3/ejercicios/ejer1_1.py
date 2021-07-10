


x = 3
n = -2

def potencia(x,n) -> float:
    p = 1.0
    if n > 0:
        for i in range(1,n+1):
            p *= x
    elif n < 0:
        for i in range(1,-n+1): #(1,-(-n)+1)
            p *= x
        p = 1.0/p
    return p

print(potencia(x,n))