'''
Resolução dos exercícios do livro "Introdução à Programação com Python - Algoritmos e Lógica de Programação para Iniciantes".
Autor: Nilo Ney Coutinho Menezes
Novatec - 4ª Edição

Programa que lê três números e mostra o maior e o menor entre eles.
Autora: Dayane Dutra (Técnico em Informática - 2° Período)
Última Modificação: 10/10/2026
Contato: dutra007@proton.me
'''

primeiro_numero = float(input("Digite o primeiro número: "))
segundo_numero = float(input("Digite o segundo número: "))
terceiro_numero = float(input("Digite o terceiro número: "))

maior = primeiro_numero
menor = primeiro_numero

if segundo_numero > maior:
    maior = segundo_numero
elif segundo_numero < menor:
    menor = segundo_numero

if terceiro_numero > maior:
    maior = terceiro_numero
elif terceiro_numero < menor:
    menor = terceiro_numero

print("-" * 50)

if primeiro_numero == segundo_numero and segundo_numero == terceiro_numero:
    print(f"Todos os números são iguais.\nNúmero digitado: {primeiro_numero}")
else:
    print(f"Maior Número: {maior}")
    print(f"Menor Número: {menor}")
