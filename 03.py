notas = []
for i in range(4):
    while True:
        try:
            entrada = float(input('Digite a nota: '))
        except ValueError:
            print('Informe apenas números reais')
        else:
            notas.append(entrada)
            break
print(f'Notas informadas: {notas}')
media = sum(notas) / len(notas)
print(f'A media é: {media}')
