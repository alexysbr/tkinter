from tkinter import *

def hello():
    #print ('Hello Mundo') 
    texto_hello["text"] = 'Hello World!'

janela = Tk()
#janela.geometry('400x400')

janela.title('1º')

texto_orientacao = Label(janela, text="Primeiro programa em Python \ncom interface gráfica Tkinter")
texto_orientacao.grid(column = 0,row = 0, padx = 10, pady = 10)

texto_orientacao = Label(janela, text="Click no botão para mais detalhes \ndo que esse programa faz")
texto_orientacao.grid(column = 0,row = 1, padx = 10, pady = 10)

botao = Button(janela, text='Click me', command=hello)
botao.grid(column = 0, row = 2, padx = 10, pady = 10)

texto_hello = Label(janela, text="")
texto_hello.grid(column = 0, row = 3, padx = 10, pady = 10)

janela.mainloop()