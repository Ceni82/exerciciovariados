'''
EXERCICIO 11 - 03/04/22 - PYTHON BRASIL
ESTRUTURA SEQUENCIAL

11. Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
        a - o produto do dobro do primeiro com metade do segundo .
        b - a soma do triplo do primeiro com o terceiro.
        c - o terceiro elevado ao cubo.

'''

num1 = int(input('Digite primeiro numero: '))
num2 = int(input('Digite segundo numero: '))
num3 = float(input('Digite terceiro numero: '))

print(f'Calcule o produto do dobro do primeiro com metade do segundo. R: {int(num1*2) + int(num2/2)})')
print(f'Calcule a soma do triplo do primeiro com o terceiro.R: {num1*3 + num3}')
print(f'Calcule  o terceiro elevado ao cubo. R: {num3 ** 3}')