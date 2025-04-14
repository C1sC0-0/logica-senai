import os
os.system("clear")

lista_notas = []

for i in range(3):
    notas = float(input("Digite uma nota: "))
    lista_notas.append(notas)

soma= sum(lista_notas)
media = soma/notas

if media>= 7:
    resultado= "Aprovado"
elif media>= 5:
    resultado= "Recuperção"
else:
    resultado= "Reprovado"

print()
for nota in lista_notas:
    print(nota)
print(f"Media: {media}")
print(f"Resultado: {resultado}")