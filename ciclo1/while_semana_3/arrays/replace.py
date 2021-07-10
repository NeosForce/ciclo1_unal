#Metodo replace: Reemplaza una subcadena x otra, 
#ejemplo: objeto.replace(anterior, nueva)
str1 = 'cien agnos de soledad'
print(str1)
rep = str1.replace('cien', 'setenta')
print(rep)
rep = rep.replace('agnos', 'dias')
print(rep)
rep = rep.replace('soledad', 'clases sincronicas!')
print(rep)
rep = rep.replace('a', '#')
print(rep)