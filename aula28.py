"""
Exercício
Peça ao usuário para digitar seu nome
Peça ao usuário para digitar sua idade
Se nome e idade forem digitados:
    Exiba:
        Seu nome é {nome}
        Seu nome invertido é {nome invertido}
        Seu nome contém (ou não) espaços
        Seu nome tem {n} letras
        A primeira letra do seu nome é {letra}
        A última letra do seu nome é {letra}
Se nada for digitado em nome ou idade: 
    exiba "Desculpe, você deixou campos vazios."
"""
#Minha versão: (ficou quase tudo certo, porém eu esqueci dos comparativos, 
#and e in)
nome = input('Digite seu nome: ')
idade = input('Digite sua idade: ')
letra = len (nome)

if nome:
    print(f'Seu nome é: {nome}')
    print(f'Seu nome invertido é: {nome[::-1]}')
    print(f'Seu nome {nome} contém espaços')
    print(f'Seu nome {nome} tem {letra} letras')
    print(f'A primeira letra do seu nome é:  {nome[0]}')
    print(f'A última letra do seu nome é:  {nome[5]}')
elif nome == ' ':
    print(f'Seu nome {nome} tem espaços')
else:
    print(f'Nome e idade vazios!')

# Versão do professor:
nome = input('Digite o seu nome: ')
idade = input('Digite sua idade: ')

if nome and idade:
    print(f'Seu nome é {nome}')
    print(f'Seu nome invertido é {nome[::-1]}')

    if ' ' in nome:
        print('Seu nome contém espaços')
    else:
        print('Seu nome NÃO contém espaços')

    print(f'Seu nome tem {len(nome)} letras')
    print(f'A primeira letra do seu nome é {nome[0]}')
    print(f'A última letra do seu nome é {nome[-1]}')
else:
    print("Desculpe, você deixou campos vazios.")