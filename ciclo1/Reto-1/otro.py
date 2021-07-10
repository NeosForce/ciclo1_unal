import math

kf = int(input("Cantidad de kilos de floculante "))
kc = (kf*2) + 4
lcl = math.floor((kf + kc) / 5)

if lcl < 20:
  consumoC = "uno"
if lcl >= 20 < 30:
  consumoC = "dos"
if lcl >= 30 < 50:
  consumoC = "tres"
if lcl > 50:
  consumoC = "cuatro"
print(kf ,kc ,lcl)
print(consumoC)