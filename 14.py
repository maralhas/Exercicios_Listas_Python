pergunta = ['Telefonou para a vítima? ','Esteve no local do crime? ','Mora perto da vítima? ','Devia para a vítima? ','Já trabalhou com a vítima? ']
resposta = []
print('Resposta [s] sim ou [n] não. ')
for i in range(len(pergunta)):
    while True:
        try:
            print(pergunta[i])
            entrada_resposta = input()
            entrada_resposta = entrada_resposta.upper()
        except ValueError:
            print('ERRO! responda novamente')
        else:
            if entrada_resposta == 'S':
                resposta.append(1)
                break
            elif entrada_resposta == 'N':
                resposta.append(0)
                break
            else:
                print('Resposra invalida.')
if sum(resposta) == 5:
    print('Assassino')
elif 3 <= sum(resposta) <= 4:
    print('Cúmplice')
elif sum(resposta) == 2:
    print('Suspeita')
else:
    print('Inocente')
