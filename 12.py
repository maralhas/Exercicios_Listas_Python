idade = []
altura = []
contador = 0
for i in range(30):
    while True:
        try:
            entrada_idade = int(input('Digite a idade: '))
        except ValueError:
            print('Informe apenas números inteiros.')
        else:
            idade.append(entrada_idade)
            break
    while True:
        try:
            entrada_altura = float(input('Digite a altura: '))
        except ValueError:
            print('Informe apenas números.')
        else:
            altura.append(entrada_altura)
            break
media_altura = sum(altura) / len(altura)
print(media_altura)
for i in range(len(altura)):
    if idade[i] > 13:
        if altura[i] < media_altura:
            contador += 1

print(f'A media de altura é {media_altura}')
print(f'A quanridade de alunos maiores de 13 anos com a altura inferior a {media_altura} é de: {contador}')