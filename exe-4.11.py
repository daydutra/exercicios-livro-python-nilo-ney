'''
Resolução dos exercícios do livro "Introdução à Programação com Python - Algoritmos e Lógica de Programação para Iniciantes".
Autor: Nilo Ney Coutinho Menezes
Novatec - 4ª Edição

Programa que aprova ou não um empréstimo bancário para compra de uma casa.
Autora: Dayane Dutra (Técnico em Informática - 2° Período)
Última Modificação: 10/10/2026
Contato: dutra007@proton.me
'''

PERCENTUAL_LIMITE_SALARIO = 0.3

valor_casa = float(input("Digite o valor da casa a ser comprada em R$: "))
salario = float(input("Digite o salário do solicitante em R$: "))
quantidade_anos = int(input("Digite a quantidade de anos a pagar: "))

prestacao = valor_casa / (quantidade_anos * 12)

print("-" * 50)

if prestacao <= salario * PERCENTUAL_LIMITE_SALARIO:
    print(f"Valor da Prestação: R$ {prestacao:.2f}")
else:
    print("O valor da prestação excedeu o limite. Não é possível realizar o empréstimo.")
