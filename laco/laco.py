import os
import time

os.system ("clear")
print ("Contagem regressiva")
i=int(input("Digite um numero: "))
for i in range (i,0,-1):
    print(f"Valor da variável i: {i}")
    time.sleep(1)