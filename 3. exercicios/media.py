import os
os.system ("clear")

nota_um = int(input("Digite sua primeira nota: "))
nota_dois = int(input("Digite sua segunda nota: "))
nota_tres = int(input("Digite sua terceira nota: "))
media = float

media = (nota_um+nota_dois+nota_tres) /3
if media >= 7:
    print (media, "Para béns")
else:
    print (media, "sefu deu")

