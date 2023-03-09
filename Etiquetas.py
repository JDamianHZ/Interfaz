from tkinter import *
from tkinter import ttk


raiz = Tk()
etqTexto = ttk.Label(raiz, text="Imagen")
etqTexto.grid()

imagen = PhotoImage(file= 'yo 2.png')

etqImagen = ttk.Label(raiz)
etqImagen.grid()
etqImagen["image"]  = imagen

etqCombinada = ttk.Label(raiz, text="Etiqueta Combinada :)", compound="center")
etqCombinada.grid()
etqCombinada[ "image" ] = imagen

raiz.mainloop()