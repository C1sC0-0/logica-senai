import os
os.system ("clear")


login: str
senha: str

login_cadastrado = "joazin_dugrau"
senha_cadastrada = "joazin1234"

login = input("Digite seu login: ")
senha = input("digite sua senha: ")

if login == login_cadastrado and senha == senha_cadastrada:
    print ("Bem-vindo")
else:
    print ("Login ou senha invalido") 
