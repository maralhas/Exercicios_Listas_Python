import os
os.system('cls')

sistemas_operacionais = ['Windows Server', 'Unix', 'Linux', 'Netware', 'Mac OS', 'Outro']
votos_sistemas = [0] * 5 
porcentagem = []
contador = 0
mais_votado = 0
index = 0
while True:
    try:
        sistema_operacional = int(input('Qual o melhor Sistema Operacional para uso em servidores? (0=fim):'))
        if sistema_operacional == 0:
            break
    except ValueError:
        print('Informe um valor entre 1 e 6 ou 0 para sair')
    else:
        if sistema_operacional > 6:
            print('Informe um valor entre 1 e 6 ou 0 para sair')
        else:
            votos_sistemas[sistema_operacional -1] += 1
            contador += 1

print('Sistema Operacional     Votos   %')
print('-------------------     -----   ---')
for i in range (len(sistemas_operacionais)):
    porcentagem.append(((votos_sistemas[i] * 100) / contador))
    print(f'{sistemas_operacionais[i]}            {votos_sistemas[i]}           {porcentagem[i]:.0f} %')
    if votos_sistemas[i] > mais_votado:
        mais_votado = votos_sistemas[i]
        index = i
print('-------------------     -----')
print(f'Total                    {contador}')
print(f'O Sistema Operacional mais votado foi o {sistemas_operacionais[index]}, com {votos_sistemas[index]} votos, correspondendo a {porcentagem[index]:.0f} % dos votos.')