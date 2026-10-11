'''
Resolução dos exercícios do livro "Introdução à Programação com Python - Algoritmos e Lógica de Programação para Iniciantes".
Autor: Nilo Ney Coutinho Menezes
Novatec - 4ª Edição

Programa que converte uma temperatura em Celsius (°C) para Fahrenheit (F).
Autora: Dayane Dutra (Técnico em Informática - 2° Período)
Última Modificação: 10/10/2026
Contato: dutra007@proton.me
'''

temperatura_celsius = float(input("Digite a temperatura em Celsius (°C): "))

temperatura_fahrenheit = (9 * temperatura_celsius) / 5 + 32

print("-" * 50)
print(f"{temperatura_celsius} °C = {temperatura_fahrenheit} F")
