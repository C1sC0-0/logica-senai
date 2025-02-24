import os
os.system ("clear")


numero_um = int(input("Digite um numero: "))
numero_dois = int(input("Digite um numero: "))

menor = min(numero_um ,numero_dois)
maior = max (numero_um , numero_dois)   

print (f"Este é o maior numero:{maior}")
print (f"Este é o menor numero:{menor}")
