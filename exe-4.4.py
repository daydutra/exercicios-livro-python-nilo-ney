'''
Resolução dos exercícios do livro "Introdução à Programação com Python - Algoritmos e Lógica de Programação para Iniciantes".
Autor: Nilo Ney Coutinho Menezes
Novatec - 4ª Edição

Programa que lê um salário e calcula o valor do aumento, dependendo do valor do salário.
Autora: Dayane Dutra (Técnico em Informática - 2° Período)
Última Modificação: 10/10/2026
Contato: dutra007@proton.me
'''

SALARIO_BASE_AUMENTO = 1250
PORCENTAGEM_AUMENTO_SUPERIOR = 0.10
PORCENTAGEM_AUMENTO_INFERIOR_IGUAL = 0.15
aumento = None

salario = float(input("Digite o salário do funcionário em R$: "))

if salario > SALARIO_BASE_AUMENTO:
    aumento = salario * PORCENTAGEM_AUMENTO_SUPERIOR
else:
    aumento = salario * PORCENTAGEM_AUMENTO_INFERIOR_IGUAL

print("-" * 50)
print(f"Salário Atual: R$ {salario:.2f}")
print(f"Valor do Aumento: R$ {aumento:.2f}")
print(f"Salário com Aumento: R$ {salario + aumento:.2f}")
