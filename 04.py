vogais = []
consoantes = []

for i in range(10):
    entrada = input('Digite uma letra: ')
    entrada = entrada.upper()
    if entrada == 'A' or entrada == 'E' or entrada == 'I' or entrada == 'O' or entrada == 'U':
        vogais.append(entrada)
    else:
        consoantes.append(entrada)
    
print(f'A quantidade de consoantes lidas: {len(consoantes)}')
print(consoantes)