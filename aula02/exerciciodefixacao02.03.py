## 3. Classificação de idade - Peça a idade de uma pessoa. Mostre: "Criança" (até 12), "Adolescente" (13 a
## 17), "Adulto" (18 a 59) ou "Idoso" (60 ou mais).

idade = int(input("Digite sua idade: "))
if idade > 0 and idade == 12:
        print ("Criança")
elif idade >= 13 and idade <= 17:
        print ("Adolescente")
elif idade >= 18 and idade <= 59:
        print ("Adulto")
elif idade >= 60 and idade <= 150:
        print ("Idoso")
    