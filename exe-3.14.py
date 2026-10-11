'''
Resolução dos exercícios do livro "Introdução à Programação com Python - Algoritmos e Lógica de Programação para Iniciantes".
Autor: Nilo Ney Coutinho Menezes
Novatec - 4ª Edição

Programa que calcula o preço a pagar por um carro alugado.
Autora: Dayane Dutra Mendes (Técnico em Informática - 2° Período)
Última Modificação: 10/10/2026
Contato: dutra007@proton.me
'''

DIARIA_CARRO = 60
PREÇO_KM_RODADO = 0.15

total_km = float(input("Digite o total de km percorridos: "))
total_dias = int(input("Digite a quantidade de dias que o carro foi alugado: "))

print("-" * 50)
print(f"Preço a pagar: R$ {total_km * PREÇO_KM_RODADO + total_dias * DIARIA_CARRO:.2f}")
