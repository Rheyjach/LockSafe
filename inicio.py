# Modulos basicos utilizados
import tkinter
import tkinter.messagebox
import sys
import sqlite3
from os.path import abspath,join

# Clase de ejecución de la interfaz
class inicio:
    def __init__(self):
        self.ventana=tkinter.Tk()
        self.ventana.geometry("700x550+333+109")
        self.ventana.iconbitmap(self.ruta_absoluta("imagenes/icono.ico"))
        self.ventana.resizable(width=False,height=False)
        self.ventana.title("LockSafe")
        self.ventana.config(bg="#A9A9A9")

        #Imagen de la aplicacion
        self.rutaImagen=tkinter.PhotoImage(file=self.ruta_absoluta("imagenes/LockSafe.png"))

        #Labels
        self.imagenPrincipal=tkinter.Label(self.ventana,image=self.rutaImagen)
        self.imagenPrincipal.config(bg="#A9A9A9",width=180,height=270)
        self.imagenPrincipal.pack(pady=15)
        self.nombreApp=tkinter.Label(self.ventana,text="LockSafe ",font=("Times New Roman",21,"bold"),bg="#A9A9A9")
        self.nombreApp.place(x=288,y=290)

        #botones
        self.botonIngresar=tkinter.Button(self.ventana,text="Ingresar",width=10,command=self.funcionIngresar)
        self.botonIngresar.config(bg="black",fg="#A9A9A9",cursor="hand2",font=("Arial",12,"bold"))
        self.botonIngresar.place(x=295,y=340)
        self.botonInformacion=tkinter.Button(self.ventana,text="Información",width=10)
        self.botonInformacion.config(bg="black",fg="#A9A9A9",cursor="hand2",font=("Arial",12,"bold"),command=self.funcionInfo)
        self.botonInformacion.place(x=295,y=380)
        self.botonAcercade=tkinter.Button(self.ventana,text="Acerca de",width=10)
        self.botonAcercade.config(bg="black",fg="#A9A9A9",cursor="hand2",font=("Arial",12,"bold"),command=self.funcionAcercade)
        self.botonAcercade.place(x=295,y=420)
        self.botonSalir=tkinter.Button(self.ventana,text="Salir",width=10)
        self.botonSalir.config(bg="black",fg="#A9A9A9",cursor="hand2",font=("Arial",12,"bold"),command=self.funcionSalir)
        self.botonSalir.place(x=295,y=460)

        #Pie de pagina
        self.pieDepagina=tkinter.Label(self.ventana,text="© 2025 - Rheyjach Arrieta",font=("Times New Roman",10,"bold"),bg="#A9A9A9")
        self.pieDepagina.place(x=274,y=525)

        # llamar funcion basica de la base de datos
        self.conectar()

        #Bucle de la interfaz
        self.ventana.mainloop()

    #funciones 
    #funcion de rutas
    def ruta_absoluta(self,ruta_relativa):
        if hasattr(sys,'_MEIPASS'):
            self.ruta_base=sys._MEIPASS
        else:
            self.ruta_base=abspath(".")
        return join(self.ruta_base,ruta_relativa)
    #funcion de creacion de base de datos y tabla
    def conectar(self):
        self.conexion=sqlite3.connect("datos.db")
        self.cursor=self.conexion.cursor()
        self.cursor.execute("CREATE TABLE IF NOT EXISTS gestion (Registro INTEGER PRIMARY KEY AUTOINCREMENT, Aplicacion TEXT NOT NULL, Contraseña TEXT NOT NULL, Fecha TEXT NOT NULL)")
        self.conexion.commit()
        self.conexion.close()
    
    #funciones de botones
    def funcionIngresar(self):
        from claves import claves
        self.ventana.destroy()
        claves()
    def funcionInfo(self):
        tkinter.messagebox.showinfo("Información","La app permite ingresar y crear contraseñas con sus aplicaciones correspondientes. " "Guarda la informacion para filtrar por fecha y aplicacion, "
                                              "ademas de poder eliminar registros. " "Todo esto para asegurar una experiencia organizada y eficiente.")
    def funcionAcercade(self):
        tkinter.messagebox.showinfo("Acerca de","La app fue creada por el Ingeniero Rheyjach Arrieta con el objetivo de desarrollar un proyecto funcional")
    def funcionSalir(self):
        self.salida=tkinter.messagebox.askokcancel("Salir","¿Desea salir de la aplicacion?")
        if self.salida==True:
            self.ventana.destroy()
        
# Este script inicia la aplicación creando una instancia de la clase 'inicio'
if __name__=='__main__':
    ejecutar=inicio()