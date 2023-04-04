"""E necessário instalar no terminal: pip install pyintaller

comando de terminal para gerar executavel é: pyinstaller --onefile --noconsole .barra invertidaHelloMundo.py nome do arquivo não pode ter espaço"""

from tkinter import *

i=0
def hello():
    #print ('Hello Mundo') 
    global i
    i+=1
    texto_hello["text"] = f'Hello World! {i}'

janela = Tk()

#tamanho da janela
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

#botao de sair do programa
#botao2 = Button(janela, text="Quit", command=janela.destroy).grid(column=1, row=0)

janela.mainloop()