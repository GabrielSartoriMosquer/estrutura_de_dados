from dataclasses import dataclass

@dataclass
class Livro:
    titulo: str
    autor: str
    ano: int
    preco: float

lista_livros = []

def adicionar_livro():

    titulo = input('Qual o título do livro? ')
    autor = input(f'Qual o autor de {titulo.upper()}? ')
    ano = int(input(f'Qual o ano de publicação de {titulo.upper()}? '))
    preco = float(input(f'Qual o preço de {titulo.upper()}? '))

    livro_teste = Livro(titulo, autor, ano, preco)
    return livro_teste

for n in range(5):
    livro = adicionar_livro()
    lista_livros.append(livro)

print(lista_livros)

def recente(livros, ano):
    recentes = []
    for livro in livros:
        if ano - livro.ano < 5:
            recentes.append(livro)
    return recentes

def caro(livros):

    caros = []
    soma = 0
    elementos = len(livros)

    for livro in livros:
        preco = livro.preco
        soma += preco
    
    media = soma/elementos

    for livro in livros:
        if livro.preco > media:
           caros.append(livro)

    return caros

livros_recentes = recente(lista_livros, 2025)
livros_caros = caro(lista_livros)

print('Livros recentes:')
print(livros_recentes)

print('Livros caros:')
print(livros_caros)