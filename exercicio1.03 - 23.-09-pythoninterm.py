# Em um sistema web, os privilégios dos operadores são modelados por conjuntos de permissões técnicas:

# Python
# permissoes_admin = {"criar", "ler", "atualizar", "deletar", "gerar_relatorio", "gerenciar_usuarios"}
# permissoes_usuario = {"ler", "criar"}
# permissoes_necessarias = {"ler", "atualizar", "gerar_relatorio"}

# Faça um programa (exercicio3.py) que:

# Verifique se as permissões do usuário comum estão TODAS contidas dentro das permissões do admin (issubset);
# Verifique se o admin possui TODAS as permissões do usuário comum (issuperset);
# Verifique se o usuário comum e o conjunto de permissões necessárias NÃO possuem nenhuma permissão em comum (isdisjoint);
# Calcule e exiba quais permissões faltam para que o usuário comum execute a operação restrita (operação de diferença);
# Calcule e exiba quais permissões o administrador possui a mais que o usuário comum (operação de diferença);
# Conceda ao usuário comum as permissões "atualizar" e "gerar_relatorio" de uma só vez, utilizando o método update();

# Após essa inclusão, teste se o usuário agora cumpre TODOS os requisitos mínimos para executar a operação
# com segurança;

# Imprima um relatório final confirmando a lista ordenada de acessos do usuário e indicando se a operação está
# "SIM" ou "NÃO" autorizada.


permissoes_admin = {"criar", "ler", "atualizar", "deletar", "gerar_relatorio", "gerenciar_usuarios"}
permissoes_usuario = {"ler", "criar"}
permissoes_necessarias = {"ler", "atualizar", "gerar_relatorio"}

# 1

usuario_no_admin = permissoes_usuario.issubset(permissoes_admin)
print(f"As permissões do usuário estão contidas no admin? {usuario_no_admin}")

# 2

admin_cobre_usuario = permissoes_admin.issuperset(permissoes_usuario)
print(f"O admin possui todas as permissões do usuário? {admin_cobre_usuario}")

# 3 

sem_intersecao = permissoes_usuario.isdisjoint(permissoes_necessarias)
print(f"Usuário e permissões necessárias são disjuntos (sem nada em comum)? {sem_intersecao}")

# 4 - Calcular permissões que faltam para o usuário comum executar a operação restrita (diferença)
faltam_para_necessarias = permissoes_necessarias - permissoes_usuario
print(f"Permissões que faltam para o usuário nas operações necessárias: {sorted(faltam_para_necessarias)}")

# 5  - Calcular quais permissões o admin possui a mais que o usuário comum (diferença)
admin_a_mais = permissoes_admin - permissoes_usuario
print(f"Permissões que o admin possui a mais que o usuário: {sorted(admin_a_mais)}")

# 6 - - Conceder ao usuário comum as permissões "atualizar" e "gerar_relatorio" com update()
permissoes_usuario.update(["atualizar", "gerar_relatorio"])

# Após a inclusão, testar se o usuário cumpre TODOS os requisitos mínimos
cumpre_requisitos = permissoes_necessarias.issubset(permissoes_usuario)