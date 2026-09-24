## aula sobre SET´s





dev_back = {"Python", "SQL", "Docker", "Git"}     ## ----------- são listas
dev_data = {"Python", "SQL", "Pandas", "Spark"}   ## ----------- são listas

#1 união (|) -------- todas as competencias somadas
universo_dev = dev_back | dev_data    ## esse é o símbolo da UNIÃO "|" ----- vai unir as coisas que não se repetem
print ("1. União", universo_dev)

#2 Intersecção (&)  -------- me traz o que tem de comum nos CONJUNTOS

comum_dev = dev_back & dev_data
print ("2. Intersecção", comum_dev)

#3 Diferença (-)  ---------- me mostra só o que eu tenho no CONJUNTO escolhido

diferenca_dev = dev_back - dev_data
print ("3. Diferença", diferenca_dev)


#4 Simétrica  (^)  ---------- me mostra o que esta só em um e nao se repete em outras

simetrica_dev = dev_back ^ dev_data
print ("4. Simétrica", simetrica_dev)            # a virgula é para CONCATENAR a STRING com a VARIÁVEL