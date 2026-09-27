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

total_recebidos = len(cpfs)
total_unicos = len(cpfsunicos)
print(f"Total de CPFs recebidos: {total_recebidos}")
print(f"Total de CPFs únicos: {total_unicos}")

# 3

cpfs_descartados = total_recebidos - total_unicos
print(f"CPFs repetidos descartados: {cpfs_descartados}")

## 4

cpfsordenados = sorted(cpfsunicos)
print (f"CPFs em Ordem: {cpfsordenados}")

# 5 --------------- usando IF e ELSE

cpf_alvo = "12345678901"
if cpf_alvo in cpfsunicos:
    print (f" CPF presente: {cpf_alvo}")
else:
    print (f"CPF ausente: {cpf_alvo}")

# 6
cpfsunicos.add(12345678901)
cpfsunicos.discard(78945612300)

print (cpfsunicos)
