from ast import Mult
numeros_inteiros = []

for i in range(5):
    while True:
        try:
            entrada = int(input('Ditite um numero inteiro: '))
        except ValueError:
            print('Informe apenas números inteiros. ')
        else:
             numeros_inteiros.append(entrada)
             break
print(f'A soma dos numeros é {sum(numeros_inteiros)}')
print(f'A soma dos numeros é {Mult(numeros_inteiros)}')