#APP para convertir pies a metros usando tkinter
#Herrera Zepeda Jose Damian
#23/02/2023

from tkinter import *
from tkinter import ttk

#Se crea clase
class conversor:      

#init funciona como constructor   #Raiz es la tabla

    def __init__(self, raiz):
        self.pies = StringVar()
        self.metros = StringVar()


        raiz.title("Pies a metros")  #titulo de la pagina
      
        mainFrame= ttk.Frame(raiz) #widget transparete hasta especificar
        mainFrame.grid(column=0, row=0)
        piesEntry= ttk.Entry(mainFrame, textvariable=self.pies)
        piesEntry.grid(column=1,row=0)

        ttk.Label(mainFrame, text="Pies").grid(column=2,row=0)
        ttk.Label(mainFrame, text="Son equivalentes a: ").grid(column=0,row=2)
        ttk.Label(mainFrame, textvariable=self.metros).grid(column=1,row=2)
        ttk.Label(mainFrame, text="Metros").grid(column=2,row=2)

        ttk.Button(mainFrame, text="calcular", command=self.calcular).grid(column=2, row=3)

        #operacion precionando una tecla
        raiz.bind("<Return>", self.calcular)

#args es para jalar un evento de un arrglo de argumentos.
    def calcular(self, *args):
      m=  float(self.pies.get()) 
      metros= m*0.3048
      print(self.metros.set(metros))
      




if __name__=="__main__":
    print("este el archivo principal.")
    print("Nada  mas se mostrara si este es el principal.")
   

