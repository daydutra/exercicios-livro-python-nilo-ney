'''
Resolução dos exercícios do livro "Introdução à Programação com Python - Algoritmos e Lógica de Programação para Iniciantes".
Autor: Nilo Ney Coutinho Menezes
Novatec - 4ª Edição

##############################################################################################################################

Programa que lê um valor em metros, converte para milímetros e mostra o resultado.
Autora: Dayane Dutra (Técnico em Informática - 2° Período)
Última Modificação: 10/10/2026
Contato: dutra007@proton.me
'''

valor_metros = float(input("Digite o valor que você deseja converter: "))

valor_milimetros = valor_metros * 1000

print("-" * 50)
print(f"{valor_metros:.2f} m = {valor_milimetros:.2f} mm.")
