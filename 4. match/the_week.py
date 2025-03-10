import os
os.system("clear") 

dia = input("Digite dia da semana: ")

match dia:
     case"1":
          print("Hoje é domingo, fim de semana")
     case"2":
        print("Hoje é segunda-feira, dia útil")
     case"3":
        print(";Hoje é terça-feira,dia útil")  
     case"4":
         print("Hoje é quarta-feira,dia útil")
     case"5":
         print("Hoje é quinta-feira,dia útil")
     case"6":
         print("Hoje é sexta-feira,dia útil")
     case"7":
          print ("Hoje é sábado, fim de semana")
        