numeros = []
par = []
impar = []

for i in range(20):
    while True:
        try:
            entrada = int(input('Digite um número: '))
        except ValueError:
            print('Imforme apenas números inteiros.')
        else:
            numeros.append(entrada)
            if entrada % 2 == 0:
                par.append(entrada)
                break
            else:
                impar.append(entrada)
                break
print(f'Os números informados são: {numeros}')
print(f'Os números pares são: {par}')
print(f'Os números impares são: {impar}')