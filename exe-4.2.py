'''
Resolução dos exercícios do livro "Introdução à Programação com Python - Algoritmos e Lógica de Programação para Iniciantes".
Autor: Nilo Ney Coutinho Menezes
Novatec - 4ª Edição

Programa que verifica se um usuário foi multado e mostra o valor da multa, em caso positivo.
Autora: Dayane Dutra (Técnico em Informática - 2° Período)
Última Modificação: 10/10/2026
Contato: dutra007@proton.me
'''

LIMITE_VELOCIDADE = 80
MULTA_POR_KM = 5

velocidade = float(input("Digite a velocidade do carro em km/h: "))

if velocidade > LIMITE_VELOCIDADE:
    print("-" * 50)
    print("Você foi multado.")
    print(f"Valor da Multa: R$ {(velocidade - LIMITE_VELOCIDADE) * MULTA_POR_KM:.2f}")
else:
    print("Velocidade dentro do limite. Você não foi multado.")
