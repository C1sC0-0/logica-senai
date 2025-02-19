import os
os.system ("clear")

idade = int(input("Digite a idade: "))

if idade < 10 :
    print ("É menor que 10")
elif idade == 10:
    print ("É igual a 10")

else:
    print ("É maior que 10")