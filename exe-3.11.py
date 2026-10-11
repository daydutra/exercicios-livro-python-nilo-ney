'''
Resolução dos exercícios do livro "Introdução à Programação com Python - Algoritmos e Lógica de Programação para Iniciantes".
Autor: Nilo Ney Coutinho Menezes
Novatec - 4ª Edição

##############################################################################################################################

Programa que calcula o desconto de uma mercadoria.
Autora: Dayane Dutra (Técnico em Informática - 2° Período)
Última Modificação: 10/10/2026
Contato: dutra007@proton.me
'''

preco = float(input("Digite o preço da mercadoria em R$: "))
percentual_desconto = float(input("Digite o percentual de desconto: "))

print("-" * 50)
print(f"Valor do Desconto: R$ {preco * percentual_desconto / 100:.2f}")
print(f"Preço a Pagar: R$ {preco - (preco * percentual_desconto / 100):.2f}")
