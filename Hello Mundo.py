from tkinter import *

def hello():
    #print ('Hello Mundo') 
    texto_hello["text"] = 'Hello Mundo'

janela = Tk()
#janela.geometry('400x400')

janela.title('Primeiro programa em py com interface gráfica Tkinter')

texto_orientacao = Label(janela, text="Click no botão para mais detalhes \ndo que esse programa faz")
texto_orientacao.grid(column = 0,row = 0, padx = 10, pady = 10)

botao = Button(janela, text='Click me', command=hello)
botao.grid(column = 0, row = 1, padx = 10, pady = 10)

texto_hello = Label(janela, text="")
texto_hello.grid(column = 0, row = 2, padx = 10, pady = 10)

janela.mainloop()