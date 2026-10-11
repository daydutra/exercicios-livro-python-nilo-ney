'''
Resolução dos exercícios do livro "Introdução à Programação com Python - Algoritmos e Lógica de Programação para Iniciantes".
Autor: Nilo Ney Coutinho Menezes
Novatec - 4ª Edição

##############################################################################################################################

Programa que lê a quantidade de dias, horas, minutos e segundos, calcula o total em segundos e mostra o resultado.
Autora: Dayane Dutra (Técnico em Informática - 2° Período)
Última Modificação: 10/10/2026
Contato: dutra007@proton.me
'''

dias = int(input("Digite a quantidade de dias: "))
horas = float(input("Digite a quantidade de horas: "))
minutos = float(input("Digite a quantidade de minutos: "))
segundos = float(input("Digite a quantidade de segundos: "))

dias_segundos = dias * 24 * 3600
horas_segundos = horas * 3600
minutos_segundos = minutos * 60

print("-" * 50)
print(f"O total em segundos é {dias_segundos + horas_segundos + minutos_segundos + segundos:.2f} seg.")
