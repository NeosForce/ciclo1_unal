pl1 = input("Letras de candidatos ")
pl2 = input("Letras de candidatos ")
vt = input("Votos!! ")
vt1 = 0
vt2 = 0
final =''
for i in vt:
    for j in range(len(pl1)):
        if i == pl1[j]:
            vt1 = vt1 + 1
        if i == pl2[j]:
            vt2 = vt2 +  1
    if vt1 == vt2:
            final += 'I'
    if vt1 > vt2:
            final += 'P'
    else:
            final += 'N'
print(final)
