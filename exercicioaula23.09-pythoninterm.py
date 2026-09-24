# EXERCICIO 1 - LIMPAR UMA LISTA DE CPF´s REPETIDOS

# Uma empresa recebeu os 8 CPFs na lista abaixo, mas alguns deles estão repetidos:
# python
# cpfs = ["12345678901", "98765432100", "12345678901", "45678912300","98765432100",
# "78945612300", "12345678901", "45678912300"]
# 
# Faça um programa (exercicio1.py) que:
#   
#  1. Transforme essa lista em um conjunto de CPFs únicos (set);
#  2. Mostre na tela quantos CPFs foram recebidos e quantos são únicos;
#  3. Mostre quantos CPFs repetidos foram descartados;
#  4. Coloque os CPFs únicos em ordem (usando a função sorted()) e mostre na tela;
#  5. Teste se o CPF "12345678901" está no conjunto e mostre uma mensagem confirmando ou não a presença dele;
#  6. Adicione o CPF "11122233344" usando o método add() e remova o CPF "78945612300" usando o método discard();
#   
#   Mostre o conjunto final atualizado.


# 1.1  ------------ outra forma de fazer

cpfs = ["12345678901", "98765432100", "12345678901", "45678912300","98765432100","78945612300", "12345678901", "45678912300"]

cpfsunicos = set(cpfs)          #   ------------     usando só o codigo "set" eu nao preciso digitar todos os ITENS denovo
print (cpfsunicos)
# 2  -------- usar o LEN

print (f"CPF´s Recebidos: {len (cpfs)}")   # len - usamos pra contar os itens que tem
print (f"CPF's Únicos: {len (cpfsunicos)}")

# 3



