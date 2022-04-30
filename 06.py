media_alunos = []
cont = 0
media = 0
for i in range(10):
    for a in range (4):
        while True:
            try:
                entrada = float(input(f'Digite a {a+1}ª nota do Aluno {i+1}: '))
            except ValueError:
                print('Informe apena números.')
            else:
                media += entrada
                break
            entrada = 0
    media_alunos.append(media / 4)
    if media_alunos[i] >= 7:
        cont += 1
    media = 0
print(f'Números de alinos com media maior ou igual a 7.0 é : {cont}')