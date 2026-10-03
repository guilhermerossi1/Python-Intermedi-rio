## 2. Maior de três números - Peça três números inteiros. Mostre qual é o maior. Se houver empate, avise:
##"Há valores iguais".


# Lê três números inteiros
numero1 = int(input("Digite o primeiro número: ")) ## --------- input serve para dizer que deve ser colocado um numero no terminal
numero2 = int(input("Digite o segundo número: ")) ## ---------- INT é para numeros inteiros
numero3 = int(input("Digite o terceiro número: "))

# Verifica se há valores iguais
if numero1 == numero2 or numero2 == numero3 or numero1 == numero3:
    print("Há valores iguais")

# Mostra o maior número
maior = max(numero1, numero2, numero3)  # ---------- MAX mostra o maior numero
print(f"O maior número é: {maior}")

