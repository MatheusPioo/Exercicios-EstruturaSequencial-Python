'''Faça um Programa que peça a temperatura em graus Fahrenheit, transforme e mostre a temperatura em graus Celsius.'''
print('Vamos transformar temperaturas \n')
f = float(input('Entre com o valor da temperatura em Fahrenheit: '))
c = 5 * ((f-32) / 9)
print(f'o Valor {f} em Celsius é: {c:.2f}')
