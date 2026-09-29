pilha = []

def empilhar (item):
    pilha.append (item)
    
def desempilhar ():
    if len(pilha) == 0:
        print("Erro: Pilha vazia")
        return None
    return pilha.pop()  # -------------- pop = serve para desempilhar

def ver_topo ():
    if len (pilha) ==0:
        print ("Erro: pilha vazia")
        return None
    return pilha [-1]
empilhar (10)
empilhar (20)
empilhar (30)
print ("Topo", ver_topo())
print ("Desempilhado", desempilhar ())
print ("Novo topo:", ver_topo ())
    