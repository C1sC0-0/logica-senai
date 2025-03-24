import os
os.system ("clear")

print ("Somando numeros")
media = 0

for i in range (3):
    nota = float(input(f"Digite a {i+1} nota: "))
    media +=  nota /  3

if media >= 7:
    print ("Aprovado!")

if media <=6.9 and media >=5:
    print("Recuperação")

if media <= 5:
    print ("Reprovado")

print(f"Media:{media}")

    