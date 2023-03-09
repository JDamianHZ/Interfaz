from tkinter import *
from tkinter import ttk

class interfaz2:

    def __init__(self, raiz):
     self.nombre=StringVar
     self.aPat=StringVar
     self.aMat=StringVar
     self.correo=StringVar
     self.movil=StringVar
     estado= StringVar

     raiz.title("hola")  #titulo de la pagina
     
     main_Frame= ttk.Frame(raiz, padding="10 10 30 30", width=400, height=400, relief="raised") #widget transparete hasta especificar
     main_Frame.grid(column=0, row=0)
     
     
     sub_Frame= ttk.Frame(main_Frame, padding="10 10 30 30",width=200, height=200, relief="raised") #widget transparete hasta especificar
     sub_Frame.grid(column=0, row=0)

     sub2_Frame= ttk.Frame(main_Frame, padding="10 10 30 30",width=200, height=200) #widget transparete hasta especificar
     sub2_Frame.grid(column=1, row=0)

     sub3_Frame= ttk.Frame(main_Frame, padding="10 10 30 30",width=10, height=10, relief="raised") #widget transparete hasta especificar
     sub3_Frame.grid(column=0, row=1, pady=10)

     sub4_Frame= ttk.Frame(main_Frame, padding="10 10 30 30",width=10, height=10) #widget transparete hasta especificar
     sub4_Frame.grid(column=1, row=1)

     sub5_Frame= ttk.Frame(main_Frame, padding="10 10 30 30",width=10, height=10) #widget transparete hasta especificar
     sub5_Frame.grid(column=0, row=3)
     
    

     piesEntry= ttk.Entry(sub_Frame,width=22, textvariable=self.nombre)
     piesEntry.grid(column=1,row=0)
     ttk.Label(sub_Frame, text=" ").grid(column=0,row=1)
     piesEntry= ttk.Entry(sub_Frame,width=22, textvariable=self.aPat)
     piesEntry.grid(column=1,row=2)
     ttk.Label(sub_Frame, text=" ").grid(column=0,row=3)
     piesEntry= ttk.Entry(sub_Frame,width=22, textvariable=self.aMat)
     piesEntry.grid(column=1,row=4)
     ttk.Label(sub_Frame, text=" ").grid(column=0,row=5)
     piesEntry= ttk.Entry(sub_Frame,width=22, textvariable=self.correo)
     piesEntry.grid(column=1,row=6)
     ttk.Label(sub_Frame, text=" ").grid(column=0,row=7)
     piesEntry= ttk.Entry(sub_Frame, width=22, textvariable=self.movil)
     piesEntry.grid(column=1,row=8)
     
     
     

     ttk.Label(sub_Frame, text="Nombre: ").grid(column=0,row=0)
     ttk.Label(sub_Frame, text=" ").grid(column=0,row=1)    
     ttk.Label(sub_Frame, text="A.Paterno: ").grid(column=0,row=2)
     ttk.Label(sub_Frame, text=" ").grid(column=0,row=3)
     ttk.Label(sub_Frame, text="A.Materno: ").grid(column=0,row=4)
     ttk.Label(sub_Frame, text=" ").grid(column=0,row=5)
     ttk.Label(sub_Frame, text="Correo: ").grid(column=0,row=6)
     ttk.Label(sub_Frame, text=" ").grid(column=0,row=7)
     ttk.Label(sub_Frame, text="Movil: ").grid(column=0,row=8)


     ttk.Radiobutton(sub2_Frame,text="Estudiante").grid(column=0,row=0,sticky=(W,E,N,S))
     ttk.Radiobutton(sub2_Frame,text="Empleado").grid(column=0,row=1,sticky=(W,E,N,S))
     ttk.Radiobutton(sub2_Frame,text="Desempleado").grid(column=0,row=2,sticky=(W,E,N,S))


     ttk.Label(sub3_Frame, text="Aficiones ").grid(column=0,row=0)
     ttk.Checkbutton(sub3_Frame,text="Leer").grid(column=0,row=1)
     ttk.Checkbutton(sub3_Frame,text="Musica").grid(column=1,row=1)
     ttk.Checkbutton(sub3_Frame,text="Videojuegos").grid(column=2,row=1)

     comboEstados= ttk.Combobox(sub4_Frame, textvariable=estado)
     comboEstados.grid()
     comboEstados['values']=("Jalisco", "Nayarit", "Colima", "Michoacan")


     ttk.Button(sub5_Frame, text="Guardar").grid(column=0, row=0,padx=20)
     ttk.Button(sub5_Frame, text="Cancelar").grid(column=1, row=0,padx=20)


