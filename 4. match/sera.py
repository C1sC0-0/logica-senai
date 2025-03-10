import os
os.system("clear") 


valor_pagar = float(input("Digite o valor da conta:"))
pagamento = int(input(""" 
1 -À vista 
2 -Parcelado
Digite a forma de pagamento: """))


match pagamento:
    case 1:
        desconto = valor * 0.1
        valor

    case 2:
        quantidade_parcela = int(input("Digite a quantidade de parcela:"))
        if quantidade_parcela >= 1 and quantidade_parcela <= 6:
            valor_parcela = valor_parcela / quantidade_parcela

            print(f"\nValor do produto: R$")
        ...

    case _:
        print("Opção invalida")