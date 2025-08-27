notas = [7.5, 8.0, 6.5]

resposta = 0

while resposta != -1:
    resposta = float(input('Digite a nota ou -1 para sair: '))
    if resposta != -1:
        notas.append(resposta)

notas_acima = []   
notas_abaixo = []

for nota in notas:
    if nota >= 7:
        notas_acima.append(nota)
    else:
        notas_abaixo.append(nota)
        
if notas_acima:
    notas_acima.sort(reverse = True)
    print('Notas acima da média:')
    for n in notas_acima:
        print(f'-> {n}')
        
if notas_abaixo:
    notas_abaixo.sort(reverse = True)
    print('Notas abaixo da média:')
    for n in notas_abaixo:
        print(f'-> {n}')