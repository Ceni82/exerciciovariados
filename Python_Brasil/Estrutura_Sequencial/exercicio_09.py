'''
EXERCICIO 09 - 03/04/22 - PYTHON BRASIL
ESTRUTURA SEQUENCIAL

9. Faça um Programa que peça a temperatura em graus Fahrenheit, transforme e mostre a
temperatura em graus Celsius.
C = 5 * ((F-32) / 9).
'''

temperatura = float(input('Digite a temperatura em Fahrenheit (de 32 até 212) a ser convertida:'))

# conver = temperatura - 32

print(f'A temperatura é {(temperatura - 32) / 1.8 } °C')