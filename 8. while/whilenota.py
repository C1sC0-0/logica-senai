import os
os.system ("cls")

for i in range(3):
    login = input("Digite login:")
    senha = int(input("digite a senha"))
    if login !='open' or senha!= 1234:
        print("Login ou senha incorreto!\n")
         
    else:
        print ("Seja bem-vindo!")  
        break