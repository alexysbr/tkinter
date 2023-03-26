from tkinter import *

def hello():
    #print ('Hello Mundo') 
    texto_hello["text"] = 'Hello Mundo'

janela = Tk()

janela.title('Primeiro programa em py com interface gráfica Tkinter')

texto_orientacao = Label(janela, text="Click no botão para mais detalhes do que esse pro")
texto_orientacao.grid(column = 0,row = 0)

botao = Button(janela, text='click', command=hello)
botao.grid(column = 0, row = 1)

texto_hello = Label(janela, text="")
texto_hello.grid(column = 0, row = 2)

janela.mainloop()