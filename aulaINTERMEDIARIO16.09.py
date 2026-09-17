"""""

# DECLARACAO DE VARIAVEIS


nome_funcionario = "Carlos Oliveira"
horas_trabalhadas = 160
valor_hora = 12.50




#2 - CALCULO DAS HORAS TRABALHADAS


salario_mensal = horas_trabalhadas * valor_hora




#3 - EXIBIR NOME DO FUNCIONARIO, HORAS TRABALHADAS, VALOR DA HORA >> VALOR A RECEBER


print ("Nome do Funcionário: ", nome_funcionario)
print ("Horas Trabalhadas: ",horas_trabalhadas), "| Valor da hora: R$", valor_hora
print ("Valor a receber: R$", salario_mensal)

""" ""

pao_qtd = int(input("Quantidade de pães: "))
preco_pao = 0.75

cafe_qtd = int (input("Quantidade de café: "))
preco_cafe = 4.50

# CÁLCULO DO PEDIDO
total = (cafe_qtd * preco_cafe) + (pao_qtd * preco_pao)

print (f"Pedido: {pao_qtd} pães e {cafe_qtd} cafés")        ## o "f" é para O f antes das aspas serve para criar uma f-string (string formatada) em Python.
print (f"Total a pagar: R$ {total:2.f}")                  ## o "2.f" é para colocar a quantidade de numeros depois do ponto -- ex desse caso: 14.00 (o 00 sao os 2. que coloquei, se fosse 3.f seria 14.000)