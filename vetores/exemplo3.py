import os
os.system ("clear")
lista_numeros=[]
quantidade_numeros = 6
j=0
k=0
print("=Solicitando números=")
for i in range(quantidade_numeros):
    numero = int(input(f"Digite o {i+1}º número: "))
    lista_numeros.append(numero)

print(f"\Mostrando números")
for i, numero in enumerate(lista_numeros, start=1):
    print(f"{i}º número: {numero}")
    if numero %2 !=0:
        j+=1
    if numero %2 ==0:
        k+=1

print (f"Pares: {j}")
print (f"Impares: {k}")