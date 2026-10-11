'''
Resolução dos exercícios do livro "Introdução à Programação com Python - Algoritmos e Lógica de Programação para Iniciantes".
Autor: Nilo Ney Coutinho Menezes
Novatec - 4ª Edição

Programa que calcula a redução do tempo de vida de um fumante.
Autora: Dayane Dutra Mendes (Técnico em Informática - 2° Período)
Última Modificação: 10/10/2026
Contato: dutra007@proton.me
'''

PERDA_VIDA_POR_CIGARRO = 10

quantidade_cigarros_dia = int(input("Digite a quantidade de cigarros fumados por dia: "))
tempo_fumante = int(input("Digite a quantidade de anos em que você é fumante: "))

total_dias = tempo_fumante * 365

print("-" * 50)
print(f"Você já perdeu {quantidade_cigarros_dia * PERDA_VIDA_POR_CIGARRO * total_dias / 1440:.1f} dias de vida.")
