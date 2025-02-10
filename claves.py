# Modulos basicos utilizados
import tkinter
import tkinter.messagebox
import tkinter.ttk
import sqlite3
from os.path import abspath,join
import sys
from datetime import date
from random import shuffle,choice

# Clase de ejecución de la interfaz
class claves:
    def __init__(self):
        self.ventana=tkinter.Tk()
        self.ventana.geometry("700x550+333+109")
        self.ventana.iconbitmap(self.ruta_absoluta("imagenes/icono.ico"))
        self.ventana.resizable(width=False,height=False)
        self.ventana.title("LockSafe")
        self.ventana.config(bg="#A9A9A9")
        
        #Barra de menu
        self.barraMenu=tkinter.Menu(self.ventana)
        self.ventana.config(menu=self.barraMenu)
        self.barraMenu.add_command(label="Info",command=self.info)
        self.barraMenu.add_command(label="Acerca de",command=self.acercade)
        self.barraMenu.add_command(label="Salir",command=self.salir)

        #labels
            #ingresar contraseñas
        self.labelIngreso=tkinter.Label(self.ventana,text="Ingreso de contraseña",bg="#A9A9A9",font=("Arial",14,"bold"))
        self.labelIngreso.place(x=20,y=10)
        self.labelAplicacion1=tkinter.Label(self.ventana,text="Aplicacion",bg="#A9A9A9",font=("Arial",13,"bold"))
        self.labelAplicacion1.place(x=20,y=50)
        self.labelClave=tkinter.Label(self.ventana,text="Contraseña",bg="#A9A9A9",font=("Arial",13,"bold"))
        self.labelClave.place(x=20,y=80)
            #crear contraseñas
        self.labelCrear=tkinter.Label(self.ventana,text="Crear contraseña",bg="#A9A9A9",font=("Arial",14,"bold"))
        self.labelCrear.place(x=360,y=10)
        self.labelAplicacion2=tkinter.Label(self.ventana,text="Aplicacion",bg="#A9A9A9",font=("Arial",13,"bold"))
        self.labelAplicacion2.place(x=360,y=50)
        self.labelLongitud=tkinter.Label(self.ventana,text="Longitud",bg="#A9A9A9",font=("Arial",13,"bold"))
        self.labelLongitud.place(x=360,y=80)
            #filtros
        self.labelFiltro=tkinter.Label(self.ventana,text="Gestion de datos",bg="#A9A9A9",font=("Arial",14,"bold"))
        self.labelFiltro.place(x=20,y=410)
        self.labelFecha=tkinter.Label(self.ventana,text="Fecha",bg="#A9A9A9",font=("Arial",13,"bold"))
        self.labelFecha.place(x=20,y=450)
        self.labelAplicacion3=tkinter.Label(self.ventana,text="Aplicacion",bg="#A9A9A9",font=("Arial",13,"bold"))
        self.labelAplicacion3.place(x=360,y=450)
        self.labelEliminar=tkinter.Label(self.ventana,text="Registro",bg="#A9A9A9",font=("Arial",13,"bold"))
        self.labelEliminar.place(x=20,y=490)

        #botones
        self.botonIngresar=tkinter.Button(self.ventana,text="Ingresar",width=8,height=1,command=self.ingresar)
        self.botonIngresar.config(font=("Arial","10","bold"),background="#8EBAE2",activebackground="#8EBAE2",bd=3,cursor="hand2")
        self.botonIngresar.place(x=20,y=120)
        self.botonCrear=tkinter.Button(self.ventana,text="Crear",width=8,height=1,command=self.crear)
        self.botonCrear.config(font=("Arial","10","bold"),background="#8EBAE2",activebackground="#8EBAE2",bd=3,cursor="hand2")
        self.botonCrear.place(x=360,y=120)
        self.botonBuscar1=tkinter.Button(self.ventana,text="Buscar",width=8,height=1,command=self.buscar1)
        self.botonBuscar1.config(font=("Arial","7","bold"),background="#8EBAE2",activebackground="#8EBAE2",bd=3,cursor="hand2")
        self.botonBuscar1.place(x=255,y=450)
        self.botonBuscar2=tkinter.Button(self.ventana,text="Buscar",width=8,height=1,command=self.buscar2)
        self.botonBuscar2.config(font=("Arial","7","bold"),background="#8EBAE2",activebackground="#8EBAE2",bd=3,cursor="hand2")
        self.botonBuscar2.place(x=615,y=450)
        self.botonEliminar=tkinter.Button(self.ventana,text="Eliminar Registro",width=13,height=1,command=self.eliminar)
        self.botonEliminar.config(font=("Arial","7","bold"),background="#8EBAE2",activebackground="#8EBAE2",bd=3,cursor="hand2")
        self.botonEliminar.place(x=255,y=490)
        self.botonMostrar=tkinter.Button(self.ventana,text="Mostrar todos los Registros",width=21,height=1,command=self.cargar)
        self.botonMostrar.config(font=("Arial","7","bold"),background="#8EBAE2",activebackground="#8EBAE2",bd=3,cursor="hand2")
        self.botonMostrar.place(x=460,y=490)
        self.botonInicio=tkinter.Button(self.ventana,text="Inicio",width=8,height=1,command=self.funcionInicio)
        self.botonInicio.config(font=("Arial","10","bold"),background="#8EBAE2",activebackground="#8EBAE2",bd=3,cursor="hand2")
        self.botonInicio.place(x=615,y=120)

        #entrys
            #ingresar contraseñas
        self.entryAplicacion1=tkinter.Entry(self.ventana,font=("Arial","10","bold"),bg="white")
        self.entryAplicacion1.place(x=120,y=50)
        self.entryClave=tkinter.Entry(self.ventana,font=("Arial","10","bold"),bg="white")
        self.entryClave.place(x=120,y=80)
            #crear contraseñas
        self.entryAplicacion2=tkinter.Entry(self.ventana,font=("Arial","10","bold"),bg="white")
        self.entryAplicacion2.place(x=460,y=50)
        self.entryLongitud=tkinter.Entry(self.ventana,font=("Arial","10","bold"),bg="white")
        self.entryLongitud.place(x=460,y=80)
            #filtros
        self.entryFecha=tkinter.Entry(self.ventana,font=("Arial","10","bold"),bg="white")
        self.entryFecha.place(x=100,y=450)
        self.entryAplicacion3=tkinter.Entry(self.ventana,font=("Arial","10","bold"),bg="white")
        self.entryAplicacion3.place(x=460,y=450)
        self.entryEliminar=tkinter.Entry(self.ventana,font=("Arial","10","bold"),bg="white")
        self.entryEliminar.place(x= 100,y=490)

        #scroll
        self.scrollVertical=tkinter.Scrollbar(self.ventana, orient="vertical")
        self.scrollVertical.place(x=650,y=180,height=225)

        #Tabla
        self.tabla=tkinter.ttk.Treeview(self.ventana,columns=("Registro","Aplicacion","Contraseña","Fecha de Registro"),yscrollcommand=self.scrollVertical.set)
        self.tabla.place(x=20,y=180)
        self.tabla.heading('#1',text='Registro')
        self.tabla.heading('#2',text='Aplicacion')
        self.tabla.heading('#3',text='Contraseña')
        self.tabla.heading('#4',text='Fecha de Registro')

        self.style=tkinter.ttk.Style()
        self.style.configure("self.tabla",font=("Arial","9"))
        self.style.configure("self.tabla.heading",font=("Arial","10","bold"))

        #Desabilitar columna '#0'
        self.tabla.column('#0',width=0,stretch=tkinter.NO)

        self.tabla.column('#1',width=150,anchor="center")
        self.tabla.column('#2',width=170,anchor="center")
        self.tabla.column('#3',width=150,anchor="center")
        self.tabla.column('#4',width=150,anchor="center")

        #eventos de la tabla
        self.tabla.bind("<Button-1>", self.copiar_valor)

        # cooperacion entre scroll y barra
        self.scrollVertical.config(command=self.tabla.yview)

        # llamar funcion basica de la base de datos
        self.cargar()

        #Pie de pagina
        self.pieDepagina=tkinter.Label(self.ventana,text="© 2025 - Rheyjach Arrieta",font=("Times New Roman",10,"bold"),bg="#A9A9A9")
        self.pieDepagina.place(x=274,y=511)

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
    #funciones barra de menu
    def info(self):
        self.info=tkinter.messagebox.showinfo("Información","La app permite ingresar y crear contraseñas con sus aplicaciones correspondientes. " "Guarda la informacion para filtrar por fecha y aplicacion, "
                                              "ademas de poder eliminar registros. " "Todo esto para asegurar una experiencia organizada y eficiente")
    def acercade(self):
        self.acercade=tkinter.messagebox.showinfo("Acerca de","La app fue creada por el Ingeniero Rheyjach Arrieta con el objetivo de desarrollar un proyecto funcional")
    def salir(self):
        self.salida=tkinter.messagebox.askokcancel("Salir","¿Desea salir de la aplicacion?")
        if self.salida==True:
            self.ventana.destroy()
    
    # Funciones de conexion a base de datos
    def guardar(self,aplicacion,clave,fecha):
        self.conexion=sqlite3.connect("datos.db")
        self.cursor=self.conexion.cursor()
        self.cursor.execute("INSERT INTO gestion(Aplicacion,Contraseña,Fecha) VALUES (?,?,?)",(aplicacion,clave,fecha))
        self.conexion.commit()
        self.conexion.close()
        tkinter.messagebox.showinfo("EXITO","Datos guardados exitosamente")

    def cargar(self):
        #limpiar tabla
        for self.row in self.tabla.get_children():
            self.tabla.delete(self.row)
        #consultar y cargar datos
        self.conexion=sqlite3.connect("datos.db")
        self.cursor=self.conexion.cursor()
        self.cursor.execute("SELECT * FROM gestion")
        self.filas=self.cursor.fetchall()
        self.conexion.close()

        for self.fila in self.filas:
            self.tabla.insert("","end",values=self.fila)

    #funciones de botones
    def funcionInicio(self):
        from inicio import inicio
        self.ventana.destroy()
        inicio()
    def ingresar(self):
        self.variableAplicacion1=self.entryAplicacion1.get()
        self.variableClave=self.entryClave.get()
        if  not self.variableAplicacion1.strip() or not  self.variableClave.strip():
            tkinter.messagebox.showerror("AVISO","Las entradas de Aplicacion y Contraseña tienen que estar llenas para poder ingresar los datos al sistema")
        else:
            if len(self.variableAplicacion1.strip())>25 or len(self.variableClave.strip()) >12 or len(self.variableClave.strip())<4:
                tkinter.messagebox.showinfo("CONSIDERACION","La Aplicacion debe tener maximo 25 caracteres y la Contraseña debe tener maximo 12 y minimo 4 caracteres")
            else:
                self.fechaActual=str(date.today())
                self.guardar(self.variableAplicacion1.strip(),self.variableClave.strip(),self.fechaActual)
                self.cargar()
    def crear(self):
        self.variableAplicacion2=self.entryAplicacion2.get()
        self.variableLongitud=self.entryLongitud.get()
        if not self.variableAplicacion2.strip() or not self.variableLongitud.strip():
            tkinter.messagebox.showerror("AVISO","Las entradas de Aplicacion y Longitud tienen que estar llenas para poder ingresar los datos al sistema")
        else:
            if not self.variableLongitud.strip().isdigit():
                tkinter.messagebox.showerror("AVISO","La entrada Longitud solo permite valores numericos positivos")
            else:
                self.variableLongitud=int(self.variableLongitud.strip())
                if len(self.variableAplicacion2) > 25 or self.variableLongitud > 12 or self.variableLongitud < 4:
                    tkinter.messagebox.showinfo("CONSIDERACION","La Aplicacion debe tener maximo 25 caracteres y la Longitud de la contraseña debe ser de maximo 12 y minimo 4 caracteres")
                else:
                    self.numeros=[self.z for self.z in range(0,10)]
                    self.mayusculas=[chr(self.r) for self.r in range(65,91)]
                    self.minusculas=[chr(self.x) for self.x in range(97,123)]
                    self.simbolos=["#","@","$","&","%"]
                    self.clave_lista=[choice(self.numeros),choice(self.mayusculas),choice(self.minusculas),choice(self.simbolos)]
                    for self.a in range(self.variableLongitud-4):
                        self.base_completa=self.numeros+self.mayusculas+self.minusculas+self.simbolos
                        self.clave_lista.append(choice(self.base_completa))
                    shuffle(self.clave_lista)
                    self.clave="".join(map(str,self.clave_lista))
                    self.fechaActual=str(date.today())
                    self.guardar(self.variableAplicacion2.strip(),self.clave,self.fechaActual)
                    self.cargar()
        
    def buscar1(self):
        self.variableFecha=self.entryFecha.get()
        if not self.variableFecha.strip():
            tkinter.messagebox.showerror("AVISO","No hay datos ingresados para filtrar por Fecha")
        else:
            for self.row in self.tabla.get_children():
                self.tabla.delete(self.row)

            self.conexion=sqlite3.connect("datos.db")
            self.cursor=self.conexion.cursor()
            self.cursor.execute("SELECT * FROM gestion WHERE Fecha=(?)",(self.variableFecha,))
            self.filas=self.cursor.fetchall()
            self.conexion.close()

            for self.fila in self.filas:
                self.tabla.insert("","end",values=self.fila)
    def buscar2(self):
        self.variableAplicacion3=self.entryAplicacion3.get()
        if not self.variableAplicacion3.strip():
            tkinter.messagebox.showerror("AVISO","No hay datos ingresados para filtrar por Aplicacion")
        else:
            for self.row in self.tabla.get_children():
                self.tabla.delete(self.row)

            self.conexion=sqlite3.connect("datos.db")
            self.cursor=self.conexion.cursor()
            self.cursor.execute("SELECT * FROM gestion WHERE Aplicacion=?",(self.variableAplicacion3,))
            self.filas=self.cursor.fetchall()
            self.conexion.close()

            for self.fila in self.filas:
                self.tabla.insert("","end",values=self.fila)
    def eliminar(self):
        self.variableEliminar=self.entryEliminar.get()
        if not self.variableEliminar.strip():
            tkinter.messagebox.showerror("AVISO","No ha ingresado un codigo de Registro para ser eliminado")
        else:
            if not self.variableEliminar.strip().isdigit():
                tkinter.messagebox.showerror("AVISO","Solo se permiten valores numericos positivos")
            else:
                self.conexion=sqlite3.connect("datos.db")
                self.cursor=self.conexion.cursor()
                self.cursor.execute("SELECT Registro FROM gestion")
                self.filas=self.cursor.fetchall()
                self.conexion.close()
                self.registros=[self.i[0] for self.i in self.filas]

                self.variableEliminar=int(self.variableEliminar.strip())

                if self.variableEliminar not in self.registros:
                    tkinter.messagebox.showinfo("AVISO","El Registro ingresado no se encuentra almacenado")
                else:
                    self.conexion=sqlite3.connect("datos.db")
                    self.cursor=self.conexion.cursor()
                    self.cursor.execute("DELETE FROM gestion where Registro=?",(self.variableEliminar,))
                    self.conexion.commit()
                    self.conexion.close()
                    tkinter.messagebox.showinfo("EXITO",f"El Registro {self.variableEliminar} fue eliminado correctamente")
                    self.cargar()

    # Funcion de copiar valores
    def copiar_valor(self,evento):
        # Obtener el item seleccionado
        self.item = self.tabla.identify_row(evento.y)
        self.column = self.tabla.identify_column(evento.x)

        if self.item and self.column:
            self.column_index = int(self.column.replace("#", "")) - 1
            self.value = self.tabla.item(self.item)["values"][self.column_index]

            # Copiar al portapapeles
            self.ventana.clipboard_clear()
            self.ventana.clipboard_append(self.value)
            self.ventana.update()
            tkinter.messagebox.showinfo("COPIADO",f"Copiado al portapapeles: {self.value}")


