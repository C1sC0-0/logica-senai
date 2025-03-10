nome = input("Digite o nome do aluno: ")
nota1 = float(input("Digite a nota da sua primeira prova:"))
nota2 = float(input("Digite a nota da sua segunda prova:"))
resultado = (nota1 + nota2) / 2

if resultado >= 9:
    print ("Nota: A, Aprovado!")

if resultado >= 7.5 and resultado< 9:
    print("Nota: B, aprovado!")

if resultado>= 6 and resultado<7.5:
    print("Nota: C, Aprovado!")

if resultado>= 4 and resultado<6:
    print("Nota: D, reprovado!")

if resultado <4:
    print("Nota: E, reprovado!")