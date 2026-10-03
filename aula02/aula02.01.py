def criar (valor): ## ----- criando uma FUNCAO
    return {"valor": valor, "esquerda": None, "direita": None} # ----- retornando um DICIONÁRIO

def inserir (raiz, valor): # ----- criando uma FUNCAO ----- e criei variaveis VAZIAS sem ter colocado nada nelas, posso fazer isso no PYTHON
    if raiz is None: # -------- verifica SE a variavel "raiz" esta vazia
        return criar (valor)  # retorna o "NÓ" criado com o valor recebido
    if valor < raiz ["valor"]: # Checa se o valor a inserir é MENOR
        raiz ["esquerda"] = inserir (raiz["esquerda"], valor)
    elif valor > raiz ["valor"]: # checa se o valor a inserir é MAIOR
        raiz ["direita"] = inserir (raiz["direita"], valor) 
        return raiz # retorna a referencia do "NÓ" atualizado
    
    def buscar (raiz, valor) # Criando a FUNÇÃO "BUSCAR"
        if raiz is None:
            return False # encerra a busca
        if raiz ["valor"] == valor:
            return True
        if valor < raiz ["valor"]: # percorre o lado esquerdo
            return buscar(raiz["esquerda"], valor)
        else: # percorre o lado direito
            return buscar (raiz["direita"], valor)    
        
        arvore = None
        valores =[50, 30, 70, 20, 40, 60, 80]
        
        for v in valores:
            arvore = inserir (arvore, v)
            print (f"\n --- Apos inserir {v} ---")
            
        print (f"\n Em ordem")