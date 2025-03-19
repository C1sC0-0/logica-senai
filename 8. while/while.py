import os
os.system ("cls")

contador= 0
continua= 's'

while continua=='s':
#comandos a serem repetidos
    print("Repetindo....")
    contador +=1
    continua= input ("Tecle 's' desejo:").strip().lower()

if contador == 0:
    input ("O bloco NÃO foi repetido")
else:
    print(f"o bloco foi repetido{contador}vezes")