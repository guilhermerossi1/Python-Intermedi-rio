# Exercício 4 — Comparar o estoque de duas lojas (com proteção contra erros)

# Crie um programa (exercicio4.py) contendo uma função chamada 

# analisar_inventario(inventario_loja_a,
# inventario_loja_b) que atenda às seguintes especificações:

# Apresente uma docstring completa documentando o propósito da função, seus parâmetros de entrada, tipos de retorno e exceções tratadas;

# Utilize um bloco try-except para validar se ambos os parâmetros passados podem ser convertidos em conjuntos. Se algum argumento não for iterável, a função deve exibir uma mensagem explicativa do erro e retornar None;

# A função deve retornar um dicionário estruturado com as seguintes chaves de auditoria: "produtos_comuns":

# conjunto dos itens encontrados em ambas as lojas;
# "produtos_exclusivos_a": conjunto dos itens presentes apenas no estoque da Loja A;
# "produtos_exclusivos_b": conjunto dos itens presentes apenas no estoque da Loja B;
# "total_catalogo_unificado": número inteiro com a contagem geral de produtos únicos da rede;
# "duplicatas_descartadas_a": número inteiro de itens repetidos removidos da carga da Loja A;
# "duplicatas_descartadas_b": número inteiro de itens repetidos removidos da carga da Loja B.

# Teste a função chamando-a com os seguintes dados de estoque: 

# loja_a = ["notebook", "mouse", "teclado", "monitor", "mouse", "notebook", "webcam"]
# loja_b = ["teclado", "monitor", "impressora", "scanner", "teclado"]

# Percorra o dicionário retornado e exiba cada chave acompanhada do seu valor (garanta que todos os conjuntos sejam impressos como listas ordenadas alfabeticamente para facilitar a leitura);

# Realize uma chamada de teste enviando propositalmente um valor inválido (como o número inteiro 10 no lugar de uma lista) para demonstrar a eficácia do tratamento de exceções sem interrupção abrupta do programa.

def analisar_inventario(inventario_loja_a, inventario_loja_b):
    """
    Analisa e compara o estoque de duas lojas, calculando itens comuns, exclusivos,
    tamanho do catálogo unificado e contagem de duplicatas descartadas.

    Parâmetros:
        inventario_loja_a (iterable): Lista ou iterável com os produtos da Loja A.
        inventario_loja_b (iterable): Lista ou iterável com os produtos da Loja B.

    Retorno:
        dict: Dicionário contendo as chaves de auditoria e métricas de estoque,
              ou None caso ocorra erro nos parâmetros.

    Exceções Tratadas:
        TypeError: Caso os argumentos passados não sejam iteráveis.
    """
    try:
        # Tenta converter as entradas para listas para contagem de duplicatas originais
        lista_a = list(inventario_loja_a)
        lista_b = list(inventario_loja_b)
        
        conjunto_a = set(lista_a)
        conjunto_b = set(lista_b)
        
    except (TypeError, ValueError) as e:
        print(f"[Erro de Validação] Os dados fornecidos não são válidos ou iteráveis: {e}")
        return None

    # Cálculo das métricas de auditoria
    produtos_comuns = conjunto_a & conjunto_b
    produtos_exclusivos_a = conjunto_a - conjunto_b
    produtos_exclusivos_b = conjunto_b - conjunto_a
    
    catalogo_unificado = conjunto_a | conjunto_b
    total_catalogo_unificado = len(catalogo_unificado)
    
    duplicatas_a = len(lista_a) - len(conjunto_a)
    duplicatas_b = len(lista_b) - len(conjunto_b)

    resultado = {
        "produtos_comuns": produtos_comuns,
        "produtos_exclusivos_a": produtos_exclusivos_a,
        "produtos_exclusivos_b": produtos_exclusivos_b,
        "total_catalogo_unificado": total_catalogo_unificado,
        "duplicatas_descartadas_a": duplicatas_a,
        "duplicatas_descartadas_b": duplicatas_b
    }

    return resultado


# --- Testes do Exercício 4 ---

loja_a = ["notebook", "mouse", "teclado", "monitor", "mouse", "notebook", "webcam"]
loja_b = ["teclado", "monitor", "impressora", "scanner", "teclado"]

print("--- Teste com dados válidos ---")
auditoria = analisar_inventario(loja_a, loja_b)

if auditoria:
    for chave, valor in auditoria.items():
        # Se o valor for um conjunto, imprime como lista ordenada alfabeticamente conforme pedido
        if isinstance(valor, set):
            print(f"{chave}: {sorted(valor)}")
        else:
            print(f"{chave}: {valor}")

print("\n--- Teste com dados inválidos (tratamento de exceção) ---")
# Enviando propositalmente o inteiro 10 no lugar de uma lista
analisar_inventario(10, loja_b)