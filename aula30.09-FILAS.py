from collections import deque   # ------- aqui ta importando a biblioteca de filas

fila_impressao = deque () # ---- criando a fila e impressao

fila_impressao.append ("Relatorio.pdf") # ---- adicionando itens na fila
fila_impressao.append ("contrato.docx") 
fila_impressao.append ("vendas.xlsx")

print ("Fila:", list (fila_impressao)) # --- o codigo "list" vai converter a lista para exibição

documento = fila_impressao.popleft() # --- o "pop.left" vai tirar o primeiro da fila // e no caso se eu quiser usar só "pop" - ele vai tirar o ultimo
print ("Imprimindo agora:", documento)
print ("Próximo da fila:", fila_impressao [0])