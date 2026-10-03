def criar_no(valor):
    return {"valor": valor, "esquerda": None, "direita": None}

def inserir(raiz, valor):
    if raiz is None:
        return criar_no(valor)
    if valor < raiz["valor"]:
        raiz["esquerda"] = inserir(raiz["esquerda"], valor)
    elif valor > raiz["valor"]:
        raiz["direita"] = inserir(raiz["direita"], valor)
    return raiz

def buscar(raiz, valor):
    if raiz is None:
        return False
    if raiz["valor"] == valor:
        return True
    if valor < raiz["valor"]:
        return buscar(raiz["esquerda"], valor)
    return buscar(raiz["direita"], valor)

def em_ordem(no, resultado):
    if no is not None:
        em_ordem(no["esquerda"], resultado)
        resultado.append(no["valor"])
        em_ordem(no["direita"], resultado)
    return resultado

def exibir(no, nivel=0):
    if no is not None:
        exibir(no["direita"], nivel + 1)
        print("    " * nivel + str(no["valor"]))
        exibir(no["esquerda"], nivel + 1)


# ---- EXECUCAO ----
arvore = None
valores = [50, 30, 70, 20, 40, 60, 80]

for v in valores:
    arvore = inserir(arvore, v)

print("=== ARVORE MONTADA ===")
exibir(arvore)

print("\nEm-ordem (crescente):", em_ordem(arvore, []))
print("Busca 40:", buscar(arvore, 40))
print("Busca 99:", buscar(arvore, 99))