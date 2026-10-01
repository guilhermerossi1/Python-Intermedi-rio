from collections import deque

fila = deque () # cria a fila que receberá os nomes

def enfileirar (item): # criando funçao para "enfileirar" 
    fila.append (item) # adiciona o item no inicio da fila
    
def desenfileirar (): # funcao desenfileirar
    if len(fila) == 0: # Verifica se a fila está vazia antes de tirar um item
        print ("Erro: a fila está vazia!")
        return None
    return fila.popleft () # Se a fila tiver antes, elimina um item

def primeiro (): # Função de ver o primeiro da fila
    if len (fila) == 0 : # LEN - conta a quantidade de itens na "fila" e compara com o "0"
        print ("Erro: a fila está vazia!")
        return None
    return fila [0] # ---- esse RETURN é como se fosse o "else"

enfileirar ("Ana")
enfileirar ("Bruno")
enfileirar ("Carla")

print ("Fila: ", list (fila)) # ---- Exibe FILA em formato de lista
print ("Primeiro: ", primeiro ()) # ---- Exibe primeira pessoa da fila
print ("Atendido: ", desenfileirar ()) # ---- Exibe função desenfileirar
print ("Próximo: ", primeiro ()) # ---- Exibe o primeiro - próximo (no caso)

