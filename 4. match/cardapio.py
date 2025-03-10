opcao = int(input("""
Codigo \t Prato \t\t\t Valor                  
1 \t Picanha \t\t R$25,00                   
2 \t Lasanha \t\t R$20,00
3 \t Strogonoof \t\t R$ 18,00                  
4 \t Bife acebolado \t R$ 15,00                  
5 \t Pão com ovo \t\t R$ 5,00 

Digite a opção desejada:                 
"""))



match opcao:
    case "1":
        print("Prato selecionado:Picanha R$:25,00")
    
    case "2":
        print("Prato selecionado:Lasanha R$:20,00")
    
    case "3":
        print("Prato selecionado:Strogonoff R$:18,00 ")
    
    
    case "4":
        print("Prato selecionado:Bife acebolado R$:15,00")
    
    case "5":
        print("Prato selecionado:Pão com ovo R$:5,00")


print(f"Prato selecionado")
