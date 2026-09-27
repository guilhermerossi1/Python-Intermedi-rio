# Exercício 2 — Quem comprou em quais canais?

# Uma loja realiza vendas em seu espaço físico, no site e em um marketplace parceiro. A relação de compradores
# de cada canal está registrada nos seguintes conjuntos:

# python
# clientes_loja = {"Alice", "Bob", "Carlos", "Diana", "Eduardo"}
# clientes_site = {"Bob", "Diana", "Fernanda", "Gabriel", "Helena"}
# clientes_marketplace = {"Alice", "Fernanda", "Igor", "Bob", "Julia"}

# Faça um programa (exercicio2.py) que descubra e mostre na tela a quantidade de pessoas e a lista de nomes em ordem alfabética para:

# 1 - Todas as pessoas que compraram em pelo menos UM dos canais;
# 2 - As pessoas que compraram simultaneamente nos TRÊS canais disponíveis;
# 3 - As pessoas que compraram EXCLUSIVAMENTE na loja física (sem compras no site ou marketplace);
# 4 - As pessoas que compraram em exatamente DOIS canais de venda;
# 5 - As pessoas que compraram em apenas UM canal (clientes de canal exclusivo em todo o negócio).

# Dica: utilize os operadores de conjuntos | (união), & (interseção), - (diferença) e ^ (diferença simétrica).

clientes_loja = {"Alice", "Bob", "Carlos", "Diana", "Eduardo"}
clientes_site = {"Bob", "Diana", "Fernanda", "Gabriel", "Helena"}
clientes_marketplace = {"Alice", "Fernanda", "Igor", "Bob", "Julia"}

# 1 - usar UNIAO "|"

clientes_geral = clientes_loja | clientes_site | clientes_marketplace
print (f"Os clientes no geral são: {clientes_geral}")

# 2 - usar INTERSEÇAO (&)

clientes_simultaneos = clientes_loja & clientes_site & clientes_marketplace
print (f"Os clientes simultâneos são: {clientes_simultaneos}")

# 3 ---- usar DIFERENÇA (-)

clientes_exclusivos = clientes_loja - clientes_site - clientes_marketplace
print (f"Os clientes exclusivos são: {clientes_exclusivos}")

# 4

dois_canais = (
    (clientes_loja & clientes_site)
    | (clientes_loja & clientes_marketplace)
    | (clientes_site & clientes_marketplace)
) - clientes_simultaneos
print(f"Exatamente dois canais ({len(dois_canais)} pessoas): {sorted(dois_canais)}")

# 5

exclusivo_loja_sozinha = clientes_loja - clientes_site - clientes_marketplace
exclusivo_site_sozinho = clientes_site - clientes_loja - clientes_marketplace
exclusivo_mkt_sozinho = clientes_marketplace - clientes_loja - clientes_site

print (exclusivo_loja_sozinha)
print (exclusivo_site_sozinho)
print (exclusivo_mkt_sozinho)