'''
Resolução dos exercícios do livro "Introdução à Programação com Python - Algoritmos e Lógica de Programação para Iniciantes".
Autor: Nilo Ney Coutinho Menezes
Novatec - 4ª Edição

##############################################################################################################################

Programa que calcula o aumento de um salário.
Autora: Dayane Dutra (Técnico em Informática - 2° Período)
Última Modificação: 10/10/2026
Contato: dutra007@proton.me
'''

salario = float(input("Digite o valor do salário em R$: "))
porcentagem_aumento = float(input("Digite a porcentagem do aumento: "))

print("-" * 50)
print(f"Valor do Aumento: R$ {salario * porcentagem_aumento / 100:.2f}")
print(f"Novo Salário: R$ {salario + (salario * porcentagem_aumento / 100):.2f}")
