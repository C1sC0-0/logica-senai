import os
def logo_senai():
    os.system("clear")
    print("==SENAI==")

def calcular_media(primeiro_numero,segundo_numero):
    soma= primeiro_numero + segundo_numero
    return soma
logo_senai()
primeira_nota = int(input("Digite a primeira nota: "))
segunda_nota = int(input("Digite a segunda nota nota: "))
soma= calcular_media(primeira_nota, segunda_nota)
logo_senai()
print(f"Soma:{soma}")