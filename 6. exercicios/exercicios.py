import os
os.system("clear")

matriculas = float(input("Digite o numero da sua matricula: "))
idade = int(input("Digite sua idade: "))
tempo_trabalhado = int(input("Digite seu tempo de trabalho"))
nascimento = 2025 - idade

print (f"O código do empregado é: {matriculas:}")
print (f" O empregado tem: {idade} anos")
print(f"O empregado nasceu em: {nascimento}")
print (f"O tempo trabalhado: {tempo_trabalhado}")


if idade > 65 or tempo_trabalhado > 30:
    print("Pode se aposentar.")
elif idade < tempo_trabalhado:
    print("Dados incorretos>")

else:
    print("NÃO pode se aposentar.")