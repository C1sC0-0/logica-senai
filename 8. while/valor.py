import os
os.system ("cls")
i = 0
notas=0

numero = int(input("Digite um numero: "))

while True:
    numero = int(input("Digite um numero: "))
    
    if numero <0:
        break
    notas += numero
    i += 1

resultado =notas/i
print(resultado)
