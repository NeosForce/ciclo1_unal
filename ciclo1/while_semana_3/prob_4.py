#ve: Pia, Pib, ta, tb
#vs: n (n es el agno cuando Pb> Pa)
Pia=25.E6;   Pib=18.9E6; 
ta=2./100;  tb=3./100; 
n=0
Pa=Pia;   Pb=Pib #inicializacion
while Pa > Pb:
  incrA=Pa*ta
  incrB=Pb*tb
  Pa += incrA # cuerpo
  Pb += incrB  
  n+=1
print(n, Pa, Pb, sep='\t\t')