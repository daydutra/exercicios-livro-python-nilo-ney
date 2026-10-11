'''
Resolução dos exercícios do livro "Introdução à Programação com Python - Algoritmos e Lógica de Programação para Iniciantes".
Autor: Nilo Ney Coutinho Menezes
Novatec - 4ª Edição

Programa que lê três números e mostra o maior e o menor entre eles.
Autora: Dayane Dutra Mendes (Técnico em Informática - 2° Período)
Última Modificação: 10/10/2026
Contato: dutra007@proton.me
'''

maior = None
menor = None

primeiro_numero = float(input("Digite o primeiro número: "))
segundo_numero = float(input("Digite o segundo número: "))
terceiro_numero = float(input("Digite o terceiro número: "))

if primeiro_numero > segundo_numero and segundo_numero > terceiro_numero:
    maior = primeiro_numero
    menor = terceiro_numero
elif primeiro_numero > terceiro_numero and terceiro_numero > segundo_numero:
    maior = primeiro_numero
    menor = segundo_numero
elif segundo_numero > primeiro_numero and primeiro_numero > terceiro_numero:
    maior = segundo_numero
    menor = terceiro_numero
elif segundo_numero > terceiro_numero and terceiro_numero > primeiro_numero:
    maior = segundo_numero
    menor = primeiro_numero
elif terceiro_numero > primeiro_numero and primeiro_numero > segundo_numero:
    maior = terceiro_numero
    menor = segundo_numero
elif terceiro_numero > segundo_numero and segundo_numero > primeiro_numero:
    maior = terceiro_numero
    menor = primeiro_numero

print("-" * 50)
print(f"Maior Número: {maior}")
print(f"Menor Número: {menor}")
