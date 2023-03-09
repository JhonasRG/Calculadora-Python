import sys

num1 = int(input("Insira o primeiro número: "))
num2 = int(input("Insira o segundo número: "))
operacao = input("[S]ubtração -- [A]dição -- [M]ultiplicação -- \
[D]ivisão: \n")

def calculadora(operacao=operacao):
    resultado = 0
    def multiplicar(num1, num2):
        resultado = num1 * num2
        return resultado
    
    def somar(num1, num2):
        resultado = num1 + num2
        return resultado
    
    def dividir(num1, num2):
        resultado = num1 / num2
        return resultado
    
    def subtrair(num1, num2):
        resultado = num1 - num2
        return resultado
    
    if operacao == 'S':
        return subtrair
    elif operacao == 'A':
        return somar
    elif operacao == 'M':
        return multiplicar
    elif operacao == 'D':
        return dividir

calcular = calculadora(operacao)
print(calcular(num1, num2))