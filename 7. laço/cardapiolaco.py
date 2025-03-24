import os
os.system("cls")

comanda=0
while True:
    print("""
            Codigo \t Prato \t\t\t Valor                  
            1 \t Picanha \t\t R$25,00                   
            2 \t Lasanha \t\t R$20,00
            3 \t Strogonoof \t\t R$ 18,00                  
            4 \t Bife acebolado \t R$ 15,00                  
            5 \t Pão com ovo \t\t R$ 5,00 
""")
    opcao = (input("Digite o numero da opção desejada: "))
    
    match opcao:
        case '1':
            preco = 25
        case '2':
            preco = 20
        case '3':
            preco=18
        case '4':
            preco=15
        case '5':
            preco=5
        case _:    
            print("Opção invalida!")
            preco = 0

    comanda += preco
    repetir = input("\nDigite 's' se quiser adicionar mais algum prato e 'n' se nao quiser: ").lower()
    if repetir == "n":
        break
        
print(f"o total é:{comanda}")
