numeros = []

for i in range (5):
    while True:
        try:
            entrada = int(input('Informe um número: '))
        except ValueError:
            print('Informe apenas números inteiros!')
        else:
            numeros.append(entrada)
            break
print(numeros)