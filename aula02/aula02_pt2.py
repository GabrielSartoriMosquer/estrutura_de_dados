from dataclasses import dataclass

@dataclass
class Aluno:
    nome: str
    idade: int
    media: float

aluno = Aluno('Felipe', 45, 9.2)

print(aluno)