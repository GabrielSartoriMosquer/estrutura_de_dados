class Aluno:
    def __init__(self, nome, idade, media):

        self.nome = nome
        self.idade = idade
        self.media = media

        def aprovado(self):
            return self.media >= 7
        
    
gabriel = Aluno('Gabriel', 18, 6)

print(gabriel.idade)