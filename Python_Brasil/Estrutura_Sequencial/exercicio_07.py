'''

EXERCICIO 07 - 02/04/22 - PYTHON BRASIL
ESTRUTURA SEQUENCIAL

  7. Faça um Programa que calcule a área de um quadrado,
  em seguida mostre o dobro desta área para o usuário.
'''

lado = float(input('Insira a medida do quadrado:'))

area = lado ** 4
dobro = area * 2.0


print(f'Area do quadrado é {area}!')
print(f'E seu obro é {dobro}!')