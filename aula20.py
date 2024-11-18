#Minha forma de resolver
primeiro_valor = input('Digite o primeiro valor: ')
segundo_valor = input('Digite o segundo valor: ')

if segundo_valor > primeiro_valor:
    print(f'{segundo_valor}  é maior que o primeiro_valor= {primeiro_valor}')
elif primeiro_valor > segundo_valor:
    print(f'{primeiro_valor}  é maior que o segundo_valor= {segundo_valor}')
else:
    print('Digite algum valor!')


#Forma de resolver do professor
primeiro_valor = input('Digite um valor: ')
segundo_valor = input('Digite outro valor: ')

if primeiro_valor >= segundo_valor:
    print(
        f'{primeiro_valor=} é maior ou igual '
        f'ao que {segundo_valor=}'
    )
else:
    print(
        f'{segundo_valor=} é maior '
        f'do que {primeiro_valor=}'
    )
    