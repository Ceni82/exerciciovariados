'''
EXERCICIO 08 - 02/04/22 - PYTHON BRASIL
ESTRUTURA SEQUENCIAL

8. Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês.
    Calcule e mostre o total do seu salário no referido mês.


'''

ganhos_hora = float(input("Quanto vc ganha por hora? "))
horas_trabalhadas = float(input("Quantas horas vc trabalha por mês?"))

# calculo = ganhos_hora * horas_trabalhadas

print(f'Seu salario mensal é de R$ {ganhos_hora*horas_trabalhadas :.2f}')