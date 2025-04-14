import os
os.system ("clear")

def calcular_imc(peso, altura):
    return peso / (altura* altura)
def situacao(imc):
    if imc >=40:
        classificacao= "Obesidade grau III"
        recomendacao= "Busque assistencia médica imediatamente"
    elif imc >=35:
        classificacao= "Obesidade grau II"
        recomendacao= "Busque um m[edico para avaliação e orientação"
    elif imc >=30:
        classificacao= "Obesidade grau I"
        recomendacao= "Procure a orientação de um profissional"
    elif imc >=25:
        classificacao= "Sobrepeso"
        recomendacao= "Considere hábitos saudáveis"
    elif imc >=18.5:
        classificacao= "Peso normal"
        recomendacao= "Considere hábitos saudáveis"
    else:
        classificacao= "Abaixo do peso"
        recomendacao= "Procure um nutricionista"

peso= float(input("Digite seu peso: "))
altura= float(input("Digite sua altura em metros "))

imc = calcular_imc(peso, altura)
classificacao, recomendacao = situacao