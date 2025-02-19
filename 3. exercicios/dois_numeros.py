import os
os.system ("clear")


numero = float(input("Digite um numero: "))
segundo_numero = float(input("Digite um segundo numero: "))

soma = numero + segundo_numero
media = soma/ 2
produto = numero * segundo_numero

print (f"Soma: {soma}")
print(f"media: {media}")
print (f"Produto: {produto}")
if numero< segundo_numero:
    print ("Este é o menor numero ",numero )
    print ("Este é o maior numero ",segundo_numero)
else: 
    print ("Este é o menor numero ",segundo_numero)
    print ("Este é o maior numero ",numero)