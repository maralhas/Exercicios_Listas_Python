numeros = []

for i in range (10):
    while True:
        try:
            entrada = int(input('Informe um número: '))
        except ValueError:
            print('Informe apenas números inteiros!')
        else:
            numeros.append(entrada)
            break
numeros = numeros[::-1]
print(numeros)