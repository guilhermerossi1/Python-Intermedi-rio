## Aprovação por nota - Peça a nota de um aluno (0 a 10). Se for maior ou igual a 7, mostre "Aprovado".
## Se for entre 5 e 6.9, mostre "Recuperação". Se for menor que 5, mostre "Reprovado".

nota = 11
if nota >= 7 and nota <= 10: 
    print ("Aprovado")
elif nota > 5 and nota <= 6.9:
    print ("Recuperação")
elif nota < 5:
    print ("Reprovado")
elif nota > 10:
    print ("ERRO!")

