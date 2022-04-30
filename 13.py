temperatura = []

for i in range (12):
    while True:
        try:
            entrada_temperatura = float(input(f'Digite a temperatura media do mês {i+1}: '))
        except ValueError:
            print('Informe somente números.')
        else:
            temperatura.append(entrada_temperatura)
            break

media_anual = sum(temperatura) / len(temperatura)
print(f'Media anual: {media_anual}')

for i in range (len(temperatura)):
    if temperatura[i] > media_anual:
        if i == 0:
            print(f'1 - Janeiro: {temperatura[i]}º')
        elif i == 1:
            print(f'2 - Fevereiro: {temperatura[i]}º')
        elif i == 2:
            print(f'3 - Março: {temperatura[i]}º')
        elif i == 3:
            print(f'4 - Abril: {temperatura[i]}º')
        elif i == 4:
            print(f'5 - Maio: {temperatura[i]}º')
        elif i == 5:
            print(f'6 - Junho: {temperatura[i]}º')
        elif i == 6:
            print(f'7 - Julho: {temperatura[i]}º')
        elif i == 7:
            print(f'8 - Agosto: {temperatura[i]}º')
        elif i == 8:
            print(f'9 - Setempro: {temperatura[i]}º')
        elif i == 9:
            print(f'10 - Outubro: {temperatura[i]}º')
        elif i == 10:
            print(f'11 - Novembro: {temperatura[i]}º')
        elif i == 11:
            print(f'12 - Dezempro: {temperatura[i]}º')