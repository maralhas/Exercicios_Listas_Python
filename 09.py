numeros = []
soma = 0
for i in range (10):
    while True:
        try:
            entrada_numero = int(input('Digite um número: '))
        except ValueError:
            print('Informe apenas números inteiros.')
        else:
            numeros.append(entrada_numero)
            soma += numeros[i] ** 2
            break
print(f'A soma dos quadrados é: {soma}')