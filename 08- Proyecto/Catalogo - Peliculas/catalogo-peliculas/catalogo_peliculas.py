import tkinter as tk
from client.gui_app import Frame, barra_menu

def main():
    root= tk.Tk() #Esta linea nos crea una interfaz 
    root.title("Catálogo de películas")
    #cambiar el logo de la interfaz
    root.iconbitmap('C:\workspace\curso-python\08- Proyecto\Catalogo - Peliculas\catalogo-peliculas\img\Catalogo.ico')
    root.resizable(0,0) # para hacer que la ventana se expanda a lo largo y ancho, si se pone root.resizable(0,0) no se podria modificar.
    #frame= tk.Frame(root)
    #frame.pack()
    #frame.config(width=500, height=340, bg= "gray")
    barra_menu(root)
    #campos_peliculas(root)
    app=Frame(root= root)
    
    app.mainloop()

if __name__ == '__main__':
    main()
    