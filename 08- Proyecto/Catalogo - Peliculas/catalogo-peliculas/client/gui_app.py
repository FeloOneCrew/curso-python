from tkinter import Label, ttk
import tkinter as tk
from tkinter import messagebox
from Model.pelicula_dao import crear_tabla, borrar_tabla
from Model.pelicula_dao import Pelicula, guardar, listar, editar, eliminar


def barra_menu(root):
    barra_menu= tk.Menu(root) #Creando un objeto para la barra menu y se ancla al root.
    root.config(menu= barra_menu, width= 300, height= 300)
    
    menu_inicio= tk.Menu(barra_menu, tearoff= 0)
    barra_menu.add_cascade(label= 'Inicio', menu= menu_inicio)
    
    menu_inicio.add_command(label='Crear registro en DB', command= crear_tabla)
    menu_inicio.add_command(label='Eliminar registro en DB', command= borrar_tabla)
    menu_inicio.add_command(label='Salir', command= root.destroy) #command= root.destroy para que se le de en salir se cierre la aplicacion.
    
    
    """barra_menu.add_cascade(label= 'Consultas')
    barra_menu.add_cascade(label= 'Configuración')
    barra_menu.add_cascade(label= 'Ayuda')
    """
    
class Frame(tk.Frame):
    def __init__(self, root= None):
        super().__init__(root,width= 500, height= 340)
        self.root= root
        self.pack()
        #self.config(bg= "gray")
        self.id_pelicula = None
        self.campos_peliculas()
        self.Desahabilitar_Campos()
        self.tabla_Peliculas()

    def campos_peliculas(self):
        #Label de cada campo.
        self.lblNombre= tk.Label(self, text='Nombre: ')
        self.lblNombre.config(font= ('Arial', 12, 'bold'))
        self.lblNombre.grid(row= 0, column= 0, padx= 10, pady= 10)
        
        self.lblDuracion= tk.Label(self, text='Duración: ')
        self.lblDuracion.config(font= ('Arial', 12, 'bold'))
        self.lblDuracion.grid(row= 1, column= 0, padx= 10, pady= 10)
        
        self.lblGenero= tk.Label(self, text='Género: ')
        self.lblGenero.config(font= ('Arial', 12, 'bold'))
        self.lblGenero.grid(row= 2, column= 0, padx= 10, pady= 10)
        
        #Entrys de cada campo
        self.nombre = tk.StringVar()
        self.EntNombre= tk.Entry(self, textvariable= self.nombre)
        self.EntNombre.config(width=50 , font= ('Arial', 12))
        self.EntNombre.grid(row= 0, column= 1, padx= 10, pady= 10, columnspan=2)
        
        self.Duracion = tk.StringVar()
        self.mi_Duracion= tk.Entry(self, textvariable= self.Duracion)
        self.mi_Duracion.config(width=50 , font= ('Arial', 12))
        self.mi_Duracion.grid(row= 1, column= 1, padx= 10, pady= 10, columnspan= 2)
        
        self.Genero = tk.StringVar()
        self.EntGenero= tk.Entry(self, textvariable= self.Genero)
        self.EntGenero.config(width=50 , font= ('Arial', 12))
        self.EntGenero.grid(row= 2, column= 1, padx= 10, pady= 10, columnspan= 2)
        
        #Boton nuevo
        self.btnNuevo= tk.Button(self, text= 'Nuevo', command= self.habilitar_Campos)
        self.btnNuevo.config(width= 20, font= ('Arial', 12, 'bold'), fg= 'white', 
                             bg= '#C70039', cursor= 'hand2', activebackground= '#FEA2BD') #Configuracion del boton
        self.btnNuevo.grid(row= 3, column= 0, padx= 10, pady= 10)
        
        #Boton Guardar
        self.btnGuardar= tk.Button(self, text= 'Guardar', command= self.guardar_datos)
        self.btnGuardar.config(width= 20, font= ('Arial', 12, 'bold'), fg= 'white', 
                             bg= '#17A589', cursor= 'hand2', activebackground= '#76D7C4') #Configuracion del boton
        self.btnGuardar.grid(row= 3, column= 1, padx= 10, pady= 10)
        
       #Boton Cancelar 
        self.btnCancelar= tk.Button(self, text= 'Cancelar', command= self.Desahabilitar_Campos)
        self.btnCancelar.config(width= 20, font= ('Arial', 12, 'bold'), fg= 'white', 
                             bg= '#D4AC0D', cursor= 'hand2', activebackground= '#F9E79F') #Configuracion del boton
        self.btnCancelar.grid(row= 3, column= 2, padx= 10, pady= 10)

        
    def habilitar_Campos(self):
        #habilitar campos para escribir
        self.EntNombre.config(state= "normal")
        self.EntDuracion.config(state= "normal")
        self.EntGenero.config(state= "normal")
    
        #habilitar botones
        self.btnGuardar.config(state= "normal")
        self.btnCancelar.config(state= "normal")
    
    def Desahabilitar_Campos(self):
        #Deshabilitar campos para escribir
        self.id_pelicula = None
        self.nombre.set('') #Para que ponga el campo vacio
        self.Duracion.set('')
        self.Genero.set('')
        
       # self.EntNombre.config(state= "disabled")
        #self.EntDuracion.config(state= "disabled")
        #self.EntGenero.config(state= "disabled")
        
        #Desabilitar botones
        self.btnGuardar.config(state= "disabled")
        self.btnCancelar.config(state= "disabled")
    
    def guardar_datos(self):
        
        if self.mi_nombre.get() == "" or self.mi_Duracion.get() == "" or self.mi_Genero.get() == "" :
            
            titulo = 'Verificar datos'
            mensaje = 'Alguno de los campos esta vacio'
            messagebox.showerror(titulo, mensaje)
            
        else:
            try:
                if float(self.mi_Duracion.get())<= 0:
                    
                    titulo = 'Verificar datos'
                    mensaje = 'Por favor ingresar números mayores a 0'
                    messagebox.showerror(titulo, mensaje)
                
                else:
                    pelicula = Pelicula(
                        self.mi_nombre.get(),
                        self.mi_Duracion.get(),
                        self.mi_Genero.get()
                    )
                    
                
                    if self.id_pelicula == None:
                        guardar(pelicula)
    
                    else:
                        editar(pelicula, self.id_pelicula)
                        
                    self.tabla_Peliculas()
                    #Deshabilitar campos
                    self.Desahabilitar_Campos()
            except:
                    titulo = 'Verificar datos'
                    mensaje = 'Por favor ingresar en el campo duració números, no texto'
                    messagebox.showerror(titulo, mensaje)
            
    
    def tabla_Peliculas(self):
        #Recuperar la tabla de peliculas
        self.lista_peliculas = listar()
        self.lista_peliculas.reverse()
        
        self.tabla= ttk.Treeview(self, columns= ('Nombre','Duración','Género'))
        self.tabla.grid(row=4, column=0, columnspan= 4, padx= 10, pady= 10) #columnspan se expanda esta la columna 4
        
        self.tabla.column('Nombre',anchor='center')
        self.tabla.column('Duración',anchor='center')
        self.tabla.column('Género',anchor='center')
        
        #Scrollbar para la tabla si excede 10 registros
        self.scroll= ttk.Scrollbar(self, orient= 'vertical', command= self.tabla.yview)
        self.scroll.grid(row=4, column=4, sticky= 'nse')
        self.tabla.configure(yscrollcommand= self.scroll.set)
        
        self.tabla.heading('#0', text='Id', anchor= 'center') # '#0' EL NUMERO DE LA COLUMNA CON EL ENCABEZADO
        self.tabla.heading('#1', text='Nombre', anchor= 'center')
        self.tabla.heading('#2', text='Duración', anchor= 'center')
        self.tabla.heading('#3', text='Género', anchor= 'center')
        
        #Iterar la lista de peliculas
        
        for p in self.lista_peliculas:

            self.tabla.insert('',0, text=p[0], 
                          values=(p[1], p[2], p[3])) #Insertando datos
        
        #Insertar una imagen
        """self.imagen = tk.PhotoImage(file='C:\workspace\curso-python\08- Proyecto\Catalogo - Peliculas\catalogo-peliculas\img\danner.png')            
        li = Label(self, image=self.imagen, bg="black")
        li.grid(row= 5, column= 0,padx= 10, pady= 5, columnspan=3)
        """
        
        #Boton Editar
        self.btnEditar= tk.Button(self, text= 'Editar', command= self.editar_datos)
        self.btnEditar.config(width= 20, font= ('Arial', 12, 'bold'), fg= 'white', 
                             bg= '#A6ACAF', cursor= 'hand2', activebackground= '#E5E7E9') #Configuracion del boton
        self.btnEditar.grid(row= 6, column= 0, padx= 10, pady= 10)
        
        #Boton Eliminar
        self.btnEliminar= tk.Button(self, text= 'Eliminar', command= self.eliminar_datos)
        self.btnEliminar.config(width= 20, font= ('Arial', 12, 'bold'), fg= 'white', 
                             bg= '#34495E', cursor= 'hand2', activebackground= '#AEB6BF') #Configuracion del boton
        self.btnEliminar.grid(row= 6, column= 1, padx= 10, pady= 10)
            
    def editar_datos(self):
        try:
            self.id_pelicula= self.tabla.item(self.tabla.selection())['text']
            self.nombre_pelicula= self.tabla.item(self.tabla.selection())['values'][0]
            self.duracion_pelicula= self.tabla.item(self.tabla.selection())['values'][1]
            self.genero_pelicula= self.tabla.item(self.tabla.selection())['values'][2]
            
            self.habilitar_Campos()
            
            self.EntNombre.insert(0, self.nombre_pelicula)
            self.EntDuracion.insert(0, self.duracion_pelicula)
            self.EntGenero.insert(0, self.genero_pelicula)
        except:
            titulo = 'Edicion de datos'
            mensaje = 'No se ha seleccionado ningun registro'
            messagebox.showerror(titulo, mensaje)
        
    def eliminar_datos(self):
        
        try:
            self.id_pelicula= self.tabla.item(self.tabla.selection())['text']
            
            eliminar(self.id_pelicula)
            self.tabla_Peliculas()
            self.id_pelicula= None

        except:
            titulo = 'Eliminar un registro'
            mensaje = 'No se ha seleccionado ningun registro'
            messagebox.showerror(titulo, mensaje)
            
        