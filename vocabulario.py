from tkinter import *
from random import randint
from time import sleep

vocabulario = ('inu',  'neko', 'usagui', 'kame', 'namazu', 'baadii', 'mendori', 'niwatori', 'tori',)
combinado = ('cão', 'gato', 'coelho', 'tartaruga', 'bagre', 'passarinho', 'galinha', 'frango', 'passaro')

janela = Tk()
janela.title('1º')

def delete_botao(): 
    botao0.destroy() 

cont = 0
lista = [0,0,0,0,0,0,0,0]
incompleto = True
botao0 = botao1 = botao2 = botao3 = botao4 = botao5 = botao6 = botao7 = 0
botaob0 = botaob1 = botaob2 = botaob3 = botaob4 = botaob5 = botaob6 = botaob7 = 0
while incompleto:    
    indice = randint(0,7)
    if lista[indice] == 0:
        lista[indice] = 1      
        if(cont == 0):  
            botao0 = Button(janela, text = combinado[indice], command=delete_botao)
            botao0.grid(column = 0, row = cont, padx = 10, pady = 10)
        if(cont == 1):  
            botao1 = Button(janela, text = combinado[indice], command=())
            botao1.grid(column = 0, row = cont, padx = 10, pady = 10)
        if(cont == 2):  
            botao2 = Button(janela, text = combinado[indice], command=())
            botao2.grid(column = 0, row = cont, padx = 10, pady = 10)
        if(cont == 3):  
            botao3 = Button(janela, text = combinado[indice], command=())
            botao3.grid(column = 0, row = cont, padx = 10, pady = 10)
        if(cont == 4):  
            botao4= Button(janela, text = combinado[indice], command=())
            botao4.grid(column = 0, row = cont, padx = 10, pady = 10)
        if(cont == 5):  
            botao5 = Button(janela, text = combinado[indice], command=())
            botao5.grid(column = 0, row = cont, padx = 10, pady = 10)
        if(cont == 6):  
            botao6 = Button(janela, text = combinado[indice], command=())
            botao6.grid(column = 0, row = cont, padx = 10, pady = 10)
        if(cont == 7):  
            botao7 = Button(janela, text = combinado[indice], command=())
            botao7.grid(column = 0, row = cont, padx = 10, pady = 10)
        cont += 1
        #print(f'{lista}')
    if cont == 8:
        incompleto = False

cont = 0
lista = [0,0,0,0,0,0,0,0]
incompleto = True
while incompleto:    
    indice = randint(0,7)
    if lista[indice] == 0:
        lista[indice] = 1        
        if(cont == 0):  
            botaob0 = Button(janela, text = combinado[indice], command=delete_botao)
            botaob0.grid(column = 1, row = cont, padx = 10, pady = 10)
        if(cont == 1):  
            botaob1 = Button(janela, text = combinado[indice], command=())
            botaob1.grid(column = 1, row = cont, padx = 10, pady = 10)
        if(cont == 2):  
            botaob2 = Button(janela, text = combinado[indice], command=())
            botaob2.grid(column = 1, row = cont, padx = 10, pady = 10)
        if(cont == 3):  
            botaob3 = Button(janela, text = combinado[indice], command=())
            botaob3.grid(column = 1, row = cont, padx = 10, pady = 10)
        if(cont == 4):  
            botaob4= Button(janela, text = combinado[indice], command=())
            botaob4.grid(column = 1, row = cont, padx = 10, pady = 10)
        if(cont == 5):  
            botaob5 = Button(janela, text = combinado[indice], command=())
            botaob5.grid(column = 1, row = cont, padx = 10, pady = 10)
        if(cont == 6):  
            botaob6 = Button(janela, text = combinado[indice], command=())
            botaob6.grid(column = 1, row = cont, padx = 10, pady = 10)
        if(cont == 7):  
            botaob7 = Button(janela, text = combinado[indice], command=())
            botaob7.grid(column = 1, row = cont, padx = 10, pady = 10)
        cont += 1
        #print(f'{lista}')
    if cont == 8:
        incompleto = False
janela.mainloop()        
        
    
    




