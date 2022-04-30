notas = []

while True:
    entrada = input ('Digigite um numero: ')
    if entrada == '-1':
        break
    notas.append(float(entrada))

tamanho = len(notas)
print(f'Foram lidas {tamanho} notas')
print(' '.join([str(nota) for nota in notas]))
notas.reverse()

for nota in notas:
    print(nota)

soma = sum(notas)
media = soma / tamanho
print( f'Soma das notas é: {soma}')
print( f'A media das notas é: {media}')

print('Notas acima da média: ')
print(' '.join([str(nota) for nota in notas if nota > media]))

print('Notas Abaixo de 7: ')
print(' '.join([str(nota) for nota in notas if nota < 7]))

print('Encerrado o programa.')