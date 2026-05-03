entrada = input("Digite o código do crachá:\n> ")
codigo_interno = entrada[4:10]
setor = entrada[-5:-2]
turno = entrada[-1]
print(codigo_interno)
print(setor)
if turno == 'M':
    print('Manha')
elif turno == 'T':
    print('Tarde')
elif turno == 'N':
    print('Noite')
else:
    print('Turno Invalido')