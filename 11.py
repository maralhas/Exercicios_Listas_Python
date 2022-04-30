vetor_1 = []
vetor_2 = []
vetor_3 = []
resultado = []

for i in range (10):
    vetor_1.append(input('Vetor 1 - Digite um elemento: '))
for i in range (10):
    vetor_2.append(input('Vetor 2 - Digite um elemento: '))
for i in range (10):
    vetor_3.append(input('Vetor 3 - Digite um elemento: '))
for i in range (10):
    resultado.append(vetor_1[i])
    resultado.append(vetor_2[i])
    resultado.append(vetor_3[i])

print(f'Vetor 1 {vetor_1}')
print(f'Vetor 2 {vetor_2}')
print(f'Vetor 3 {vetor_3}')
print(f'Resiltado {resultado}')