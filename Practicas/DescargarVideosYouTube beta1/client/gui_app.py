from tkinter import Label, PhotoImage, Variable, ttk
import tkinter as tk
from tkinter import messagebox
from pytube import YouTube
import os


def barra_menu(root):
    barra_menu= tk.Menu(root)
    root.config(menu= barra_menu, width= 300, height= 300)
    
    menu_inicio= tk.Menu(barra_menu, tearoff= 0)
    barra_menu.add_cascade(label= 'Inicio', menu= menu_inicio)
    
    menu_inicio.add_command(label='Crear registro en DB')
    menu_inicio.add_command(label='Eliminar registro en DB')
    menu_inicio.add_command(label='Salir', command= root.destroy)

class Frame(tk.Frame):
    def __init__(self, root= None):
        super().__init__(root,width= 500, height= 340)
        self.root= root
        self.pack()
        self.config(bg= "#AFBFC0")
        self.id_pelicula = None
        self.campos_peliculas()
        self.Desahabilitar_Campos()

    def campos_peliculas(self):
        #Label de cada campo.
        self.lbllink= tk.Label(self, text= 'Ingresar el Link de Youtube: ')
        self.lbllink.config(font= ('Arial', 12, 'bold'), background='#AFBFC0')
        self.lbllink.grid(row= 0, column= 0, padx= 10, pady= 10, columnspan= 4)
        
        self.lbllistbox= tk.Label(self, text='Elije el formato para la descarga: MP3 o MP4 ')
        self.lbllistbox.config(font= ('Arial', 12, 'bold'), background= '#AFBFC0')
        self.lbllistbox.grid(row= 2, column= 0, padx= 10, pady= 10, columnspan= 4)
        
        #Entrys de cada campo
        self.mi_link = tk.StringVar()
        self.Entlink= tk.Entry(self, textvariable= self.mi_link)
        self.Entlink.config(width=50 , font= ('Arial', 12))
        self.Entlink.grid(row= 1, column= 0, padx= 10, pady= 10, columnspan= 4)
        
        #Listbox
        self.listbox=tk.Listbox(self, exportselection= False)
        items = (
            ".MP3",
            ".MP4")
        self.listbox.insert(0, *items)
        self.listbox.config(width= 20, height= 4)
        self.listbox.select_set(0)
        self.listbox.grid(row= 3, column= 0, padx= 10, pady= 10, columnspan= 4)
        
        
        #Boton Descargar
        self.btndescargar= tk.Button(self, text= 'Descargar', command= self.datolink)
        self.btndescargar.config(width= 20, font= ('Arial', 12, 'bold'), fg= 'white', 
                             bg= '#847E89', cursor= 'hand2', activebackground= '#DDD5E4') #Configuracion del boton
        self.btndescargar.grid(row= 4, column= 0, padx= 10, pady= 10)
        
        #Boton Nuevo
        self.btnNuevo= tk.Button(self, text= 'Nuevo', command= self.Desahabilitar_Campos)
        self.btnNuevo.config(width= 20, font= ('Arial', 12, 'bold'), fg= 'white', 
                             bg= '#56494C', cursor= 'hand2', activebackground= '#d1c1c5') #Configuracion del boton
        self.btnNuevo.grid(row= 4, column= 1, padx= 10, pady= 10)
        
       #Boton Salir 
        self.btnSalir= tk.Button(self, text= 'Salir', command= self.root.destroy)
        self.btnSalir.config(width= 20, font= ('Arial', 12, 'bold'), fg= 'white', 
                             bg= '#C2D3CD', cursor= 'hand2', activebackground= '#FFFFFF') #Configuracion del boton
        self.btnSalir.grid(row= 4, column= 2, padx= 10, pady= 10)
        

    def habilitar_Campos(self):
        #habilitar campos para escribir
        self.Entlink.config(state= "normal")
        self.btnNuevo.config(state= "normal")
        
        #Deshabilitar
        self.btndescargar.config(state= "disabled")
       
    
    def Desahabilitar_Campos(self):
        #Deshabilitar campos para escribir
        self.id_link = None
        self.mi_link.set('') #Para que ponga el campo vacio
        self.btnNuevo.config(state= "disabled")
        self.btndescargar.config(state= "normal")
   
    
    def datolink(self):
        self.habilitar_Campos()
        if self.mi_link.get() == "" :
            titulo = 'Verificar Link'
            mensaje = 'Por favor, ingresa un link de YouTube'
            messagebox.showerror(titulo, mensaje)
        
        else: 
            self.descarga()
        
    def itemSeleccionado(self):
        try:
            lista= self.listbox
            for self.item in lista.curselection():
                self.seleccion = tk.Label(self, text=lista.get(self.item))
                
        except:
            titulo = 'Verificar seleccion'
            mensaje = 'Por favor, elegir el formato de descarga'
            messagebox.showerror(titulo, mensaje)
                
    def descarga(self):
        self.itemSeleccionado()
        selecion= self.item
        save = 'videos/'
        link = self.mi_link.get()
        ink= str(link)
        yt= YouTube(link)
        
        if selecion == 1:
            try:
                #VIDEO
                yt.streams.filter(progressive= True, file_extension= 'mp4').order_by('resolution').desc().first().download(save)
                titulo = 'Descarga video'
                mensaje = 'El video se descargó correctamente'
                messagebox.showinfo(titulo, mensaje)
                
            except:
                titulo = 'Verificar conección'
                mensaje = 'Connection Error'
                messagebox.showinfo(titulo, mensaje)
        else :
            try:
                # Extraer solo el audio
                video = yt.streams.filter(only_audio=True).first()
                destination = 'audios/' or '.' #str(input(">> ")) or '.'
                
                # descargar audio
                out_file = video.download(output_path=destination)
                
                # guardar audio
                base, ext = os.path.splitext(out_file)
                new_file = base + '.mp3'
                os.rename(out_file, new_file)
                
                # Resultado del proceso
                titulo = 'Descarga'
                impr= yt.title + " has been successfully downloaded."
                mensaje = impr
                messagebox.showinfo(titulo, mensaje)
        
            except:
                titulo = 'Verificar Descarga'
                mensaje = 'Connection Error'
                messagebox.showerror(titulo, mensaje)

