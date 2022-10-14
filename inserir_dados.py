usuario = list()
dado = list()
for c in range(0, 5):
    dado.append(str(input('Nome: ')))
    dado.append(int(input('Idade: ')))
    usuario.append(dado[:])
    dado.clear()
print(usuario)
