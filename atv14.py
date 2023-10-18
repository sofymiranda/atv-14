# Exercício Python 14: Escreva um programa que pergunte o salário de um funcionário
# e calcule o valor do seu aumento. Para salários superiores a R$1250,00, calcule um
# aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%.
sal=float(input("Digite o salário: "))
if sal > 1250:
 print (f"Seu salário agora é de {sal+(sal*(10/100))}")
else:
 print (f"Seu salário agora é de {sal+(sal*(15/100))}")

