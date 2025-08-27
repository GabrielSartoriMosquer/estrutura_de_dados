notas = [7.5, 8.0, 6.5]
notas.append(9)

print(f'A lista contém {len(notas)} elementos.')

for nota in notas: #melhor forma de iterar
    print(nota)

for indice in range(len(notas)): #demanda de mais processamento, o que não é bom
    print(notas[indice])
    