import os
os.system("clear") 


valor = float(input("Digite o valor da conta:"))
pagamento = int(input("""" 
1 -À vista 
2 -Parcelado
Digite a forma de pagamento: """))


match pagamento:
    case 1:
        desconto = valor * 0.1
    case 2:
        ...

    case _:
        print("Opção invalida")