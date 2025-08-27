import random

notas = []

for n in range(20):
    nota = random.uniform(0,10)
    notas.append(nota)

def media(valores):
    resultado = sum(valores)/len(valores)
    return resultado

def maior_numero(valores):
    maior = valores[0]
    for valor in valores:
        if valor > maior:
            maior = valor
    return maior
notas.sort()

def menor_numero(valores):
    menor = valores[0]
    for valor in valores:
        if valor < menor:
            menor = valor
    return menor

print(f'Maior nota: {maior_numero(notas):.2f}')
print(f'Menor nota: {menor_numero(notas):.2f}')
print(f'Média das notas: {media(notas):.2f}')

