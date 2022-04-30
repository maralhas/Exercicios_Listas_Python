import os
os.system('cls')

jogador = [0] * 23
contador = 0
mais_votado = 0
index_mais_votado = 0
while True:
    try:
        numero_do_jogador = int(input('Número do jogador (0=fim):'))
        if numero_do_jogador == 0:
            break
    except ValueError:
        print('Informe um valor entre 1 e 23 ou 0 para sair')
    else:
        if numero_do_jogador > 23:
            print('Informe um valor entre 1 e 23 ou 0 para sair')
        else:
            jogador[numero_do_jogador -1] += 1 
            contador += 1
print(f'Foram computados {contador} votos. \n')
print('Jogador Votos           %')
for i in range (len(jogador)):
    if jogador[i] > 0:
        print(f'{i+1}               {jogador[i]}               {((jogador[i] * 100) / contador):.1f} %')
    if jogador[i] > mais_votado:
        mais_votado = jogador[i]
        index_mais_votado = i
print(f'O melhor jogador foi o número {index_mais_votado + 1}, com {jogador[index_mais_votado]} votos, correspondendo a {((jogador[index_mais_votado] * 100) / contador):.1f} % do total de votos.')
