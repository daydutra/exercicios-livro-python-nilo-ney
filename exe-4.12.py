'''
Resolução dos exercícios do livro "Introdução à Programação com Python - Algoritmos e Lógica de Programação para Iniciantes".
Autor: Nilo Ney Coutinho Menezes
Novatec - 4ª Edição

Programa que calcula o preço a pagar pelo fornecimento de energia elétrica.
Autora: Dayane Dutra (Técnico em Informática - 2° Período)
Última Modificação: 10/10/2026
Contato: dutra007@proton.me
'''

LIMITE_CONSUMO_RESIDENCIA = 500
PREÇO_ATE_LIMITE_CONSUMO_RESIDENCIA = 0.4
PREÇO_ACIMA_LIMITE_CONSUMO_RESIDENCIA = 0.65
LIMITE_CONSUMO_COMERCIO = 1000
PREÇO_ATE_LIMITE_CONSUMO_COMERCIO = 0.55
PREÇO_ACIMA_LIMITE_CONSUMO_COMERCIO = 0.6
LIMITE_CONSUMO_INDUSTRIA = 5000
PREÇO_ATE_LIMITE_CONSUMO_INDUSTRIA = 0.55
PREÇO_ACIMA_LIMITE_CONSUMO_INDUSTRIA = 0.6
valor_final = None

quantidade_kwh = float(input("Digite a quantidade de energia consumida em kWh: "))

print()
print("R - Residência")
print("I - Indústria")
print("C - Comércio")

tipo_instalacao = input("Digite a opção referente ao tipo de instalação: ")
tipo_instalacao = tipo_instalacao.upper()

while tipo_instalacao != "R" and tipo_instalacao != "I" and tipo_instalacao != "C":
    print("Opção inválida.")
    tipo_instalacao = input("Digite a opção referente ao tipo de instalação: ")
    tipo_instalacao = tipo_instalacao.upper()

if tipo_instalacao == "R":
    if quantidade_kwh <= LIMITE_CONSUMO_RESIDENCIA:
        valor_final = quantidade_kwh * PREÇO_ATE_LIMITE_CONSUMO_RESIDENCIA
    else:
        valor_final = quantidade_kwh * PREÇO_ACIMA_LIMITE_CONSUMO_RESIDENCIA
elif tipo_instalacao == "I":
    if quantidade_kwh <= LIMITE_CONSUMO_INDUSTRIA:
        valor_final = quantidade_kwh * PREÇO_ATE_LIMITE_CONSUMO_INDUSTRIA
    else:
        valor_final = quantidade_kwh * PREÇO_ACIMA_LIMITE_CONSUMO_INDUSTRIA
else:
    if quantidade_kwh <= LIMITE_CONSUMO_COMERCIO:
        valor_final = quantidade_kwh * PREÇO_ATE_LIMITE_CONSUMO_COMERCIO
    else:
        valor_final = quantidade_kwh * PREÇO_ACIMA_LIMITE_CONSUMO_COMERCIO

print("-" * 50)
print(f"Valor a Pagar: R$ {valor_final:.2f}")
