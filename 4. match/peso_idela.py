import os
os.system ("clear")

altura  = float(input("Digite sua altura em metros: "))
genero = str(input("Digite seu gênero: "))
match genero:
    case "M"| "m":
        peso_ideal = (72.7 * altura) - 58
        print (f"O peso ideal é: {peso_ideal:.2f}")
    case "F" | "f":
        peso_ideal = (62.1 * altura) - 44.7
        print (f"O peso ideal é: {peso_ideal:.2f}")
    case _:
        print("Opção invalida")