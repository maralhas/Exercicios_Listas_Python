import os
os.system('cls') # use 'clear' se estiver no linux

distancia_dos_saltos = []
saltos = ['Primeiro',  'Segundo', 'Terceiro', 'Quarto', 'Quinto' ]

nome_do_atleta = input('Digite o nome do Atlêta: ')
for i in range(5):
    while True: 
        try:
            distancia_dos_saltos.append(float(input(f'{saltos[i]} salto: ')))
        except ValueError:
            print('ERRO!!! Informe apenas números.')
        else:
            break

media_dos_saltos = sum(distancia_dos_saltos) / len(distancia_dos_saltos)

print('Resultado final:')
print(f'Atleta: {nome_do_atleta}')
print('Saltos: ', end = '')
for i in range(len(distancia_dos_saltos)):
    if i <= len(distancia_dos_saltos) -2:
        print(distancia_dos_saltos[i], end = ' - ')
    else:
        print(distancia_dos_saltos[i])
print(f'Média dos saltos: {media_dos_saltos}')
