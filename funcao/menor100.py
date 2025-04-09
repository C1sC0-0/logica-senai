import os
os.system("clear")

def inflacionar(preco):
    if preco <100:
        resultado= preco * 0.9
    else:
        resultado= preco*0.8
    return resultado

preco_prouto = float(input("Digite o preço do produto: "))

preco_inflacionado = inflacionar(preco_prouto)

print(f"Preço final: {preco_inflacionado}")