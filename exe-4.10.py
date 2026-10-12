'''
Resolução dos exercícios do livro "Introdução à Programação com Python - Algoritmos e Lógica de Programação para Iniciantes".
Autor: Nilo Ney Coutinho Menezes
Novatec - 4ª Edição

Programa que lê dois números, realiza uma operação e mostra o resultado.
Autora: Dayane Dutra (Técnico em Informática - 2° Período)
Última Modificação: 10/10/2026
Contato: dutra007@proton.me
'''

OPCAO_SOMA = 1
OPCAO_SUBTRACAO = 2
OPCAO_MULTIPLICACAO = 3
OPCAO_DIVISAO = 4

primeiro_numero = float(input("Digite o primeiro número: "))
segundo_numero = float(input("Digite o segundo número: "))

print()
print("1 - Soma (+)")
print("2 - Subtração (-)")
print("3 - Multiplicação (x)")
print("4 - Divisão (/)")

opcao = int(input("Digite a opção desejada: "))

while opcao < OPCAO_SOMA or opcao > OPCAO_DIVISAO:
    print("Opção inválida.")
    opcao = int(input("Digite a opção desejada: "))

print("-" * 50)

if opcao == OPCAO_SOMA:
    print(f"{primeiro_numero} + {segundo_numero} = {primeiro_numero + segundo_numero:.1f}")
elif opcao == OPCAO_SUBTRACAO:
    print(f"{primeiro_numero} - {segundo_numero} = {primeiro_numero - segundo_numero:.1f}")
elif opcao == OPCAO_MULTIPLICACAO:
    print(f"{primeiro_numero} x {segundo_numero} = {primeiro_numero * segundo_numero:.1f}")
else:
    print(f"{primeiro_numero} / {segundo_numero} = {primeiro_numero / segundo_numero:.1f}")
