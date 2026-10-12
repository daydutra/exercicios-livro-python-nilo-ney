'''
Resolução dos exercícios do livro "Introdução à Programação com Python - Algoritmos e Lógica de Programação para Iniciantes".
Autor: Nilo Ney Coutinho Menezes
Novatec - 4ª Edição

Programa que calcula o preço da passagem dependendo da distância.
Autora: Dayane Dutra (Técnico em Informática - 2° Período)
Última Modificação: 10/10/2026
Contato: dutra007@proton.me
'''

DISTANCIA_BASE = 200
PRECO_KM_ATE_DISTANCIA_BASE = 0.5
PRECO_KM_ACIMA_DISTANCIA_BASE = 0.45

distancia = float(input("Digite a distância da viagem em km: "))

print("-" * 50)

if distancia <= DISTANCIA_BASE:
    print(f"Valor da Passagem: R$ {distancia * PRECO_KM_ATE_DISTANCIA_BASE:.2f}")
else:
    print(f"Valor da Passagem: R$ {distancia * PRECO_KM_ACIMA_DISTANCIA_BASE:.2f}")
