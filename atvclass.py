import os 
from dataclasses import dataclass

os.system("cls||clear")
@dataclass
class pessoa:
    nome: str 
    idade: int
    peso: int
    altura: float

pessoa1 = pessoa("Marcos", 26, 75, 1.70)

print(f"Nome: {pessoa1.nome}\nIdade: {pessoa1.idade}\nPeso: {pessoa1.peso}\nAltura: {pessoa1.altura}")