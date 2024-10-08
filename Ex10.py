#Faça um Programa que peça a temperatura em graus Celsius, transforme e mostre em graus Fahrenheit.

cel = float(input('Entre com o valor em celsius: '))
f= (cel * 9/5)+32

print(f'O valor da temperatura {cel} C em Fahrenheit é: {f:.2f} F')
