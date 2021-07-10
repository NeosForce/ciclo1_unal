#El metodo count() obtiene el nro de veces que una subcadena se encuentra en una cadena 
#(o en parte de ella), un metodo es una funcion que pertenece a un objeto dado
#invocacion: obj.count(subcadena, ini, fin) ini y fin hacen referencia a inicial y final en el objeto
obj = "The avengers"
#print(obj.count('e') ,end='; ') #3
#print(obj.count('e', 0, 3),end='; ') #1  ---desde la T  hasta el 1er espacio en blanco
print(obj.count('e', 4, len(obj)), end='; ')# 2 ---desde la letra a hasta el final
cad = 'abcabcabcabcabc'
print(cad.count('abc'))