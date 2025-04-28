import os 
from dataclasses import dataclass

os.system("cls||clear")
@dataclass
class pessoa:
    nome: str 
    idade: int

@dataclass
class Pet:
    nome: str
    idade: int
    raca: str
#Atribuindo pessoa

pessoa1= pessoa("Marta", 30)
pessoa2 = pessoa("josé", 40)

pet1 = Pet("Toto", 4, "Pastor-alemão")
pet2 = Pet("Hulk", 6, "Pitbull")
print("Dados das pessoas")
print(f"Nome: {pessoa1.nome}, idade: {pessoa1.idade}")
print(f"Nome: {pessoa2.nome}, idade: {pessoa2.idade}")

print(f"Nome: {pet1.nome}, idade: {pet1.idade}, Raça: {pet1.raca}")
print(f"Nome: {pet2.nome}, idade: {pet2.idade}, Raça: {pet2.raca} ")