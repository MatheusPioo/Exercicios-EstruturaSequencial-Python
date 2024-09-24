''' Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. 
Calcule e mostre o total do seu salário no referido mês.'''
print('Calculo do salario do mes \n')
valor=float(input('Qual o valor ganho por hora? '))
hora = float(input('Qual a quantidade de horas trabalhadas no mes? '))
salario = hora * valor
print(f'O valor ganho no mes será: {salario:.2f}')
