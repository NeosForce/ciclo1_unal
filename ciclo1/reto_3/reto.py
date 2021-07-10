""" En la asamblea ordinaria de un conjunto residencial, van a elegir el consejo de administración, a partir de dos planchas: plancha 1 y plancha 2; cada plancha va a tener n candidatos, que se identifican por una letra única. Ud va a elaborar el programa para el escrutinio. Los vt solo contienen una letra que identifica a uno de los candidatos, cualquiera sea su plancha, recuerde puede haber vt en blanco también. El programa va a incrementar un contador cada que se procese un voto por la plancha 1 y va a incrementar su propio contador para la plancha 2, excepto que sea un voto en blanco.

Entradas:

línea 1: serie de las letras que identifican los integrantes de la plancha 1.

Línea 2: algo similar para la plancha 2.

Línea 3: serie de muchas letras, una por cada voto.

Las letras se ingresan juntas, es decir sin espacios entre ellas

 

Salida:

una de las letras P, N, I, se imprime cada vez que se lee públicamente el voto. Imprime la letra P si la plancha 1 tiene en ese momento mas vt que la plancha 2; Imprime N si la plancha 2 tiene en ese momento mas vt que la plancha 1; imprime la letra I, si en ese momento hay empate. """

plancha1 = input("Bienvenido, Digite la Letra unica de candidato: ")
plancha2 = input("Bienvenido, Digite la Letra unica de candidato: ")
vt = input("Bienvenido, Digite la Letra del voto por el candidato: ")
vt1 = 0
vt2 = 0
final =''
for i in vt:
    for j in range(len(plancha1)):
        if i == plancha1[j]:
            vt1 += 1
        if i == plancha2[j]:
            vt2 += 1
    if vt1 == vt2:
            final += 'I'
    if vt1 > vt2:
            final += 'P'
    if vt2 > vt1:
            final += 'N'
print(final)

