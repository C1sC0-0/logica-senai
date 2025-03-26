import os
os.system ("cls")
i = 0
j=0
k=0
numeros=0
pares=0

while True:
    numero = int(input("Digite um numero: "))
    if numero %2 !=0:
        j+=1
    if numero %2 ==0:
        k+=1
        pares+=numero
    if numero==0:
        break
    numeros +=numero
    i +=1
resultado =numeros+i
par= pares /k

print(k)
print(j)
print(par)
print(resultado)