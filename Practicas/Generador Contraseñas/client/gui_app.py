import tkinter as tk
from tkinter import ANCHOR, NW, Label, ttk
import random
from tkinter import messagebox


def barra_menu(root):
    barra_menu= tk.Menu(root)
    root.config(menu= barra_menu, width= 200, height= 200)
    
class Frame(tk.Frame):
    def __init__(self, root=None):
        super().__init__(root,width= 500, height= 340)
        self.root= root
        self.config(bg='#3e93e8')
        self.pack()
        self.campos_password()
        #self.DesahabilitarHabilitar_Campos()
    
    def campos_password(self):
        #Label de cada campo.
        self.lblContrasena= tk.Label(self, text='Número de caracteres de la contraseña: ')
        self.lblContrasena.config(font= ('Arial', 12, 'bold'),background='#BBC7A4')
        self.lblContrasena.pack(anchor=NW)
        self.lblContrasena.grid(row= 0, column= 0, padx= 10, pady= 10, columnspan= 4)
        
        
        #Label de cada campo.
        self.lblseleccion= tk.Label(self, text='Seleccione con que tipo de caracteres quiere la contraseña:(Seleccione sólo UNO)')
        self.lblseleccion.config(fg='#8eccbe',font= ('Arial', 12, 'bold'),anchor= 'center', background='#3e93e8')
        self.lblseleccion.grid(row= 2, column= 0, padx= 10, pady= 10, columnspan= 4)
  
        #Entrys de cada campo
        self.Caracteres = tk.StringVar()
        self.numCaracteres= tk.Entry(self, textvariable= self.Caracteres)
        self.numCaracteres.focus()
        self.numCaracteres.config(width=50 , font= ('Arial', 12))
        self.numCaracteres.grid(row= 1, column= 1, padx= 10, pady= 10, columnspan= 2)
        
        #Boton Generar
        self.btnGenerar= tk.Button(self, text= 'Generar', command= self.generar_password)
        self.btnGenerar.config(width= 20, font= ('Arial', 12, 'bold'), fg= 'white', 
                             bg= '#e15323', cursor= 'hand2', activebackground= '#FEA2BD') #Configuracion del boton
        self.btnGenerar.grid(row= 5, column= 0, padx= 10, pady= 10, columnspan= 2)
        
        #Boton Nuevo 
        self.btnNuevo= tk.Button(self, text= 'Nuevo', command=self.DesahabilitarHabilitar_Campos)
        self.btnNuevo.config(width= 20, font= ('Arial', 12, 'bold'), fg= 'white', 
                             bg= '#f8ab00', cursor= 'hand2', activebackground= '#F9E79F',state= "disabled") #Configuracion del boton
        self.btnNuevo.grid(row= 5, column= 1, padx= 10, pady= 10, columnspan= 2)
        
        #Boton Salir 
        self.btnSalir= tk.Button(self, text= 'Salir', command= self.root.destroy)
        self.btnSalir.config(width= 20, font= ('Arial', 12, 'bold'), fg= 'white', 
                             bg= '#42aa93', cursor= 'hand2', activebackground= '#8bcbc5') #Configuracion del boton
        self.btnSalir.grid(row= 5, column= 2, padx= 10, pady=5, columnspan= 2)
        
        #Checkbox Todos lo caracteres
        self.var1 = tk.IntVar()
        self.checkboxTodos = tk.Checkbutton(self, text="Todos", variable= self.var1, onvalue=1, offvalue=0)
        self.checkboxTodos.config(width= 20, font= ('Arial', 12, 'bold'), fg= 'Black', 
                                  cursor= 'hand2', bg= '#3e93e8')
        self.checkboxTodos.grid(row= 3, column= 0, padx= 5, pady= 10)
        
        #Checkbox solo números y letras
        self.var2 = tk.IntVar()
        self.checkboxNumLetr = tk.Checkbutton(self, text="Números y Letras", variable= self.var2, onvalue=1, offvalue=0)
        self.checkboxNumLetr.config(width= 20, font= ('Arial', 12, 'bold'), fg= 'Black', 
                                  cursor= 'hand2', bg= '#3e93e8')
        self.checkboxNumLetr.grid(row= 3, column= 1, padx= 5, pady= 10)
        
        #Checkbox solo letras
        self.var3 = tk.IntVar()
        self.checkboxLetr = tk.Checkbutton(self, text="Letras", variable= self.var3, onvalue=1, offvalue=0)
        self.checkboxLetr.config(width= 20, font= ('Arial', 12, 'bold'), fg= 'Black', 
                                  cursor= 'hand2', bg= '#3e93e8')
        self.checkboxLetr.grid(row= 3, column= 2, padx= 5, pady= 10)
        
        #Checkbox solo numeros
        self.var4 = tk.IntVar()
        self.checkboxNum = tk.Checkbutton(self, text="Números", variable= self.var4, onvalue=1, offvalue=0)
        self.checkboxNum.config(width= 20, font= ('Arial', 12, 'bold'), fg= 'Black', 
                                  cursor= 'hand2', bg= '#3e93e8')
        self.checkboxNum.grid(row= 3, column= 3, padx= 5, pady= 10)
               
        #Insertar una imagen
        self.imagen = tk.PhotoImage(file='C:\workspace\curso-python\Practicas\Generador Contraseñas\img\contraseñas-seguras.png')            
        li = Label(self, image=self.imagen, bg="#3e93e8", )
        li.grid(row= 6, column= 0,padx= 10, pady= 5, columnspan= 4)
        
    def habilitarDeshabilitar_Campos(self):
    
        #habilitar botones
        self.btnNuevo.config(state= "normal")
        self.btnGenerar.config(state= "disabled")
        self.checkboxTodos.config(state="disabled")
        self.checkboxNumLetr.config(state="disabled")
        self.checkboxLetr.config(state="disabled")
        self.checkboxNum.config(state="disabled")
        
    def DesahabilitarHabilitar_Campos(self):
        #Desabilitar botones
        self.btnNuevo.config(state= "disabled")
        self.btnGenerar.config(state= "normal")
        self.checkboxTodos.config(state="normal")
        self.checkboxNumLetr.config(state="normal")
        self.checkboxLetr.config(state="normal")
        self.checkboxNum.config(state="normal")
        
        self.var1.set(0)
        self.var2.set(0)
        self.var3.set(0)
        self.var4.set(0)
        
        self.Caracteres.set('')
        self.caract.set('')
        
        self.lblNombre.config(state= "disabled")
        self.Entcaracteres.config(state= "disabled")
        
    def contrasena_generada(self):
            self.lblNombre= tk.Label(self, text= 'La contraseña generada es: ')
            self.lblNombre.config(fg= "blue", font= ('Arial', 14, 'bold'),anchor=NW, background='#3e93e8')
            self.lblNombre.grid(row= 4, column= 0, padx= 10, pady= 10)
                            
            self.caract = tk.StringVar()
            self.Entcaracteres = tk.Entry(self, textvariable= self.caract)
            self.Entcaracteres.config(width=50 , fg='red' ,font= ('Arial', 12, 'bold'))
            self.Entcaracteres.insert(0,self.contrasena)
            self.Entcaracteres.grid(row= 4, column= 1, padx= 10, pady= 10, columnspan= 2)
            self.habilitarDeshabilitar_Campos()
        
    def generar_password(self):
        
        #Los var son lo que me indican el valor que tiene el checkbox, se fue seleccionado o no
        #Los felo, estan capturando esos valores.
        
        caracteres= self.numCaracteres.get()
        felo1= int(self.var1.get())
        felo2= int(self.var2.get())
        felo3= int(self.var3.get())
        felo4= int(self.var4.get()) 
        
        suma = felo1 + felo2 + felo3+ felo4
        
        if suma >= 2:
                titulo = 'Verificar seleccion de Checkbox'
                mensaje = 'Alerta: Has elegido varias opciones, por favor elegir sólo una'
                messagebox.showerror(titulo, mensaje)
        
        else:
            if felo1 == 1 or suma == 0 :                         
                try:
                    minus = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
                    Mayus= ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
                    Simbolos= ['/','*','-','+','%','&','°','¬','~','=','¿','|']
                    num=[1,2,3,4,5,6,7,8,9,0]
                    caract = minus + Mayus + Simbolos + num
                    self.contrasena = []
                    
                    if int(caracteres) > 20 or int(caracteres)<= 3:
                        titulo = 'Verificar tamaño de caracteres'
                        mensaje = 'Por favor, que el número de caracteres sea menor a 20 o Mayor a 3'
                        messagebox.showwarning(titulo, mensaje)
                    
                    else:
                        for i in range(int(caracteres)):
                            contra_ramdon = random.choice(caract)
                            #felo =  "".join(contra_ramdon)
                            self.contrasena.append(contra_ramdon)
                        
                        #contrasena = " ".join(contrasena) #Convertir en una cadena de caracteres
                        self.contrasena = ''.join(str(v) for v in self.contrasena)
                        self.contrasena_generada()
                        
                except:
                    titulo = 'Verificar datos'
                    mensaje = 'Por favor ingresar solo números en el campo'
                    messagebox.showerror(titulo, mensaje)
            
            else:
                if felo2 == 1:
                    try:
                        minus = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
                        Mayus= ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
                        num=[1,2,3,4,5,6,7,8,9,0]
                        caract = minus + Mayus + num
                        self.contrasena = []
                        
                        if int(caracteres) > 20 or int(caracteres)<= 3:
                            titulo = 'Verificar tamaño de caracteres'
                            mensaje = 'Por favor, que el número de caracteres sea menor a 20 o Mayor a 3'
                            messagebox.showinfo(titulo, mensaje)
                        
                        else:
                            for i in range(int(caracteres)):
                                contra_ramdon = random.choice(caract)
                                #felo =  "".join(contra_ramdon)
                                self.contrasena.append(contra_ramdon)
                            
                            #contrasena = " ".join(contrasena) #Convertir en una cadena de caracteres
                            self.contrasena = ''.join(str(v) for v in self.contrasena)
                            self.contrasena_generada()
                        
                    except:
                        titulo = 'Verificar datos'
                        mensaje = 'Por favor ingresar solo números en el campo'
                        messagebox.showerror(titulo, mensaje)
                
                else:
                    if felo3 == 1:
                        try:
                            minus = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
                            Mayus= ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
                            caract = minus + Mayus
                            self.contrasena = []
                            
                            if int(caracteres)>20 or int(caracteres)<= 3:
                                titulo = 'Verificar tamaño de caracteres'
                                mensaje = 'Por favor, que el número de caracteres sea menor a 20 o Mayor a 3'
                                messagebox.showinfo(titulo, mensaje)
                            
                            else:
                                for i in range(int(caracteres)):
                                    contra_ramdon = random.choice(caract)
                                    #felo =  "".join(contra_ramdon)
                                    self.contrasena.append(contra_ramdon)
                                    
                                #contrasena = " ".join(contrasena) #Convertir en una cadena de caracteres
                                self.contrasena = ''.join(str(v) for v in self.contrasena)
                                self.contrasena_generada()
                        
                        except:
                            titulo = 'Verificar datos'
                            mensaje = 'Por favor ingresar solo números en el campo'
                            messagebox.showerror(titulo, mensaje)
                    
                    else:
                        try:
                            num=[1,2,3,4,5,6,7,8,9,0]
                            caract = num
                            self.contrasena = []
                            
                            if int(caracteres)>20 or int(caracteres)<= 3:
                                titulo = 'Verificar tamaño de caracteres'
                                mensaje = 'Por favor, que el número de caracteres sea menor a 20 o Mayor a 3'
                                messagebox.showwarning(titulo, mensaje)
                            
                            else:
                                for i in range(int(caracteres)):
                                    contra_ramdon = random.choice(caract)
                                    #felo =  "".join(contra_ramdon)
                                    self.contrasena.append(contra_ramdon)
                                
                                #contrasena = " ".join(contrasena) #Convertir en una cadena de caracteres
                                self.contrasena = ''.join(str(v) for v in self.contrasena)
                                self.contrasena_generada()
                        
                        except:
                            titulo = 'Verificar datos'
                            mensaje = 'Por favor ingresar solo números en el campo'
                            messagebox.showerror(titulo, mensaje)