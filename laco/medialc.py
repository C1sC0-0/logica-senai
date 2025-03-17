import os
import time
os.system ("clear")

print ("Somando numeros")
media = 0

for i in range (3):
    nota = int(input(f"Digite a {i+1} nota: "))
    media +=  nota /  3

if media >= 7:
    print ("Aprovado!")
if media <7 and media >=4:
    print("Recuperação")
if media <= 4:
    print ("Reprovado")

print(f"Media:{media}")

    