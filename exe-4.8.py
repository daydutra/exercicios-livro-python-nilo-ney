'''
Resolução dos exercícios do livro "Introdução à Programação com Python - Algoritmos e Lógica de Programação para Iniciantes".
Autor: Nilo Ney Coutinho Menezes
Novatec - 4ª Edição

Programa que calcula a conta da operadora Tchau.
Autora: Dayane Dutra (Técnico em Informática - 2° Período)
Última Modificação: 10/10/2026
Contato: dutra007@proton.me
'''

OPCAO_FALOPOUCO = 1
OPCAO_FALOMUITO = 2
MINUTOS_FALOPOUCO = 100
VALOR_PLANO_FALOPOUCO = 50
PRECO_MINUTO_EXTRA_FALOPOUCO = 0.2
MINUTOS_FALOMUITO = 500
VALOR_PLANO_FALOMUITO = 99
PRECO_MINUTO_EXTRA_FALOMUITO = 0.15

print("1 - Plano Falopouco")
print("2 - Plano Falomuito")

plano = int(input("Digite a opção referente ao plano: "))

while plano < OPCAO_FALOPOUCO or plano > OPCAO_FALOMUITO:
    print("Opção inválida.")
    plano = int(input("Digite a opção referente ao plano: "))

total_minutos = int(input("Digite a quantidade de minutos consumida: "))

print("-" * 50)

if plano == OPCAO_FALOPOUCO:
    print("Você escolheu o plano Falopouco.")

    if total_minutos <= MINUTOS_FALOPOUCO:
        print(f"Valor do Plano: R$ {VALOR_PLANO_FALOPOUCO:.2f}")
    else:
        print(f"Valor do Plano: R$ {VALOR_PLANO_FALOPOUCO + (total_minutos - MINUTOS_FALOPOUCO) * PRECO_MINUTO_EXTRA_FALOPOUCO:.2f}")
else:
    print("Você escolheu o plano Falomuito.")
    
    if total_minutos <= MINUTOS_FALOMUITO:
        print(f"Valor do Plano: R$ {VALOR_PLANO_FALOMUITO:.2f}")
    else:
        print(f"Valor do Plano: R$ {VALOR_PLANO_FALOMUITO + (total_minutos - MINUTOS_FALOMUITO) * PRECO_MINUTO_EXTRA_FALOMUITO:.2f}")
