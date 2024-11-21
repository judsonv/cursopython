#minha tentativa com a ajuda do gpt
nome = 'Judson Vieira'
tamanho_nome = len(nome)

print(nome)
print(tamanho_nome)
print(nome[3])

# Substituir 'J' por 'OK' e 'S' por 'A'
nome = nome.replace('J', 'OK')
nome = nome.replace('S', 'W')

# Remover todas as ocorrências de 's'
while 's' in nome:
    nome = nome.replace('s', '', 1)
    print(nome)

print('Acabou')



