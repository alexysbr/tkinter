from tkinter import *
root = Tk() 
mylabel = Label(root, text="GeeksforGeeks") 
mylabel.pack() 
  
  
  
def delete_label(): 
    mylabel.destroy() 
  
  
B1 = Button(root, text="DELETE", command=delete_label) 
B1.pack() 
root.mainloop() 