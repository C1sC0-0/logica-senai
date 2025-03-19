import os
import time
os.system ("clear")

print ("Somando numeros")
soma = 0
for i in range (5):
    nota = int(input(f"Digite a {i+1} nota: "))
    soma = soma + nota
print(f"Soma:{soma}")

    