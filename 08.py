idade = []
altura = []

for i in range(5):
    while True:
        try:
            entrada_idade = int(input('Digite a idade: '))
        except ValueError:
            print('Informe apenas numeros inteiros.')
        else:
            idade.append(entrada_idade)
            break
    while True:
        try:
            entrada_altura = float(input('Digite a altura: '))
        except ValueError:
            print('Informe apenas numeros.')
        else:
            altura.append(entrada_altura)
            break
idade = idade[:: -1]
altura = altura[:: -1]
print(f'Idades: {idade}')
print(f'Alturas: {altura}')