import tkinter as tk 

#operações
def soma(a,b):
    return a + b 

def subtracao(a,b):
    return a - b

def multiplicacao(a,b):
    return a * b

def divisao (a,b):
    if b == 0:
        return "Erro: Divisão por 0"
    return a / b

#entradas
num1 = float(input("Digite o primeiro numero: "))
print("Digite a operação desejada: ")
print("Adição: 1")
print("subtração: 2")
print("multiplicação: 3")
print("divisão: 4")
operacao = input()
num2 = float(input("Digite o segundo numero: "))

#realizar operações
if operacao == "1":
    print("Resultado: ", soma(num1,num2))
elif operacao == "2":
    print("Resultado: ", subtracao(num1,num2))
elif operacao == "3":
    print("Resultado: ", multiplicacao(num1,num2))
elif operacao == "4":
    print("Resultado: ", divisao(num1,num2))
else:
    print ("Escolha uma operação valida")
   
    
