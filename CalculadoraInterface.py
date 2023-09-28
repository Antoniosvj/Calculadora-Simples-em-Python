import tkinter as tk

def botao_clicado(numero):
    entrada_texto.insert()

def calcular():
    calculo = entrada_texto.get()

janela = tk.TK()
janela.title("Calculadora")

entrada_texto = tk.Entry(janela, width=40)

botoes = ["C", "%", "/"
          "7", "8", "9", "*"
          "4", "5", "6", "-"
          "1", "2", "3", "+"
          "0",".","=",]