from tkinter import *


class Ops:
    INDEX = 0
    entrada_txt = 0

    def __init__(self,entrada_txt):
        self.entrada_txt=entrada_txt
        

    def click_boton(self, valor):
        self.entrada_txt.insert(self.INDEX, valor)
        self.INDEX += 1

    def click_borrar(self):
        self.entrada_txt.delete(0, END)
        self.INDEX = 0

    def operacion(self):
        aux = self.INDEX
        ecuacion = self.entrada_txt.get()
        resultado = eval(ecuacion)
        self.entrada_txt.delete(0, END)
        self.entrada_txt.insert(0, resultado)
        self.INDEX = aux + 1

