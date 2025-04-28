import os 
from dataclasses import dataclass

os.system("cls||clear")
@dataclass
class pessoa:
    nome: str 
    email: str
    telefone: float
    endereco: str
    def exibindo_dados(self):
        print("\nExibindo dados")
        print(f"Nome: {self.nome}\ne-mail:{self.email}\nTelefone: {self. telefone}\nendereço: {self.endereco}")

print ("Solicitando dados")
nome = input("Digite seu nome: ")
email = input("Digite seu e-mail: ")
telefone = input("Digite seu numero de telefone: ")
endereco = input("Digite seu endereço: ")

pessoa1 = pessoa(nome, email, telefone, endereco)
pessoa1.exibindo_dados()