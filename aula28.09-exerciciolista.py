historico = []  # ------------------- criando uma lista
historico.append("pagina_inicial.html")   # ------------- adicionando itens na lista - no caso na ultima posicao, por conta do "append"
historico.append("produtos.html")
historico.append("carrinho.html")

print ("HISTÓRICO - PILHA")
for pagina in historico [-1::-1]: # --------------- FOR = para cada "pagina" om
    print(pagina)
print ("-"*50)

print ("Historico:", historico)
pagina_atual = historico[-1]
print ("Pagina atual:",pagina_atual)
pagina_removida = historico.pop ()
print ("Voltando da página:", pagina_removida)
print ("Página atual agora:", historico [-1])
