'''
Resolução dos exercícios do livro "Introdução à Programação com Python - Algoritmos e Lógica de Programação para Iniciantes".
Autor: Nilo Ney Coutinho Menezes
Novatec - 4ª Edição

Programa que calcula o tempo de uma viagem.
Autora: Dayane Dutra Mendes (Técnico em Informática - 2° Período)
Última Modificação: 10/10/2026
Contato: dutra007@proton.me
'''

distancia = float(input("Digite a distância a ser percorrida em km: "))
velocidade_media = float(input("Digite a velocidade média esperada para a viagem em km/h: "))

print("-" * 50)
print(f"Tempo estimado para a viagem: {distancia / velocidade_media:.1f} horas.")
