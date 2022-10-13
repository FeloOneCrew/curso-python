from email.message import Message
from .conexion_db import ConexionDB
from tkinter import messagebox

def crear_tabla():
    conexion= ConexionDB()
    
    sql= '''
    CREATE TABLE peliculas(
        id_pelicula INTEGER,
        nombre VARCHAR(100),
        duracion VARCHAR(10),
        genero VARCHAR(100),
        PRIMARY KEY(id_pelicula AUTOINCREMENT)
    )'''
    
    try:
        conexion.cursor.execute(sql)
        conexion.cerrar_bd()
        
    except:
        titulo= 'Crear Registro'
        mensaje= 'La tabla en la BD, ya se encuentra creada'
        messagebox.showwarning(titulo, mensaje)

def borrar_tabla():
    conexion= ConexionDB()
    
    sql = 'DROP TABLE peliculas'
    
    try:
        conexion.cursor.execute(sql)
        conexion.cerrar_bd()
        
        titulo= 'Borrar Registro'
        mensaje= 'La  tabla en la BD, se borro con éxito'
        messagebox.showinfo(titulo, mensaje)
        
    except:
        titulo= 'Borrar Registro'
        mensaje= 'No existe tabla de datos para eliminar'
        messagebox.showerror(titulo, mensaje)
    
class Pelicula:
    def __init__(self, nombre, duracion, genero):
        
        self.idpelicula = None
        self.nombre = nombre
        self.duracion = duracion
        self.genero = genero
    
    def __str__(self):
        return f'Pelicula[{self.nombre}, {self.duracion}, {self.genero}]'
    
def guardar(pelicula):
    conexion= ConexionDB()
        
    sql= f"""INSERT INTO peliculas (nombre, duracion, genero)
    VALUES('{pelicula.nombre}','{pelicula.duracion}', '{pelicula.genero}')"""
        
    try:
        conexion.cursor.execute(sql)
        conexion.cerrar_bd()
            
        titulo= 'Ingreso de Registro'
        mensaje= 'El registro se realizó de manera éxitosa'
        messagebox.showinfo(titulo, mensaje)
            
        
    except:
        titulo= 'Error en Registro'
        mensaje= 'El registro no se realizó, ya que no existe tabla creada. Por favor crea primero la tabla'
        messagebox.showwarning(titulo, mensaje)
         
def listar():
    conexion = ConexionDB()
    
    lista_Peliculas = []
    sql = 'SELECT * FROM peliculas'
    
    try:
        conexion.cursor.execute(sql)
        lista_Peliculas = conexion.cursor.fetchall()
        conexion.cerrar_bd()
    
    except:
        titulo= 'Conexión al Registro'
        mensaje= 'Crea la tabla en la base de Datos'
        messagebox.showwarning(titulo, mensaje)
    
    return lista_Peliculas

def editar(pelicula, id_pelicula):
    conexion= ConexionDB()
    
    sql = f""" UPDATE peliculas
    SET nombre = '{pelicula.nombre}', duracion = '{pelicula.duracion}',
        genero = '{pelicula.genero}'
    WHERE id_pelicula = {id_pelicula}"""
    
    try:
        conexion.cursor.execute(sql)
        conexion.cerrar_bd()
    
    except:
        titulo= 'Edición de datos'
        mensaje= 'No se pudo realizar la edicion del registro'
        messagebox.showwarning(titulo, mensaje)
        

def eliminar(id_pelicula):
    conexion= ConexionDB()
    
    sql = f'DELETE FROM peliculas WHERE id_pelicula = {id_pelicula}'
    
    try:
        conexion.cursor.execute(sql)
        conexion.cerrar_bd()
    
    except:
        titulo= 'Eliminar datos'
        mensaje= 'No se pudo eliminar el registro'
        messagebox.showwarning(titulo, mensaje)