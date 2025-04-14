import os
os.system ("clear")
lista_numeros=[]
quantidade_numeros = 5

print("=Solicitando números=")
for i in range(quantidade_numeros):
    numero = int(input(f"Digite o {i+1}º número"))
    lista_numeros.append(numero)

maior = max(lista_numeros)
menor = min(lista_numeros)


print(f"\Mostrando números")
for i, numero in enumerate(lista_numeros, start=1):
    print(f"{i}º número: {numero}")

print(f"\Maior número: {maior}")
print(f"\Menor número: {menor}")