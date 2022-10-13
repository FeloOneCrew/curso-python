""" 
Probablemente conozcas el sistema de "me gusta" de Facebook y otras páginas. Las personas pueden "gustar" publicaciones de blog, imágenes u otros elementos. Queremos crear el texto que debe mostrarse junto a dicho elemento.

Implemente la función que toma una matriz que contiene los nombres de las personas a las que les gusta un artículo. Debe devolver el texto de la pantalla como se muestra en los ejemplos:

[]                                -->  "no one likes this"
["Peter"]                         -->  "Peter likes this"
["Jacob", "Alex"]                 -->  "Jacob and Alex like this"
["Max", "John", "Mark"]           -->  "Max, John and Mark like this"
["Alex", "Jacob", "Mark", "Max"]  -->  "Alex, Jacob and 2 others like this"

"""

def likes(names):
    # your code here
    elementos = len(names)
    if elementos == 0:
        return print("'no one likes this'")
    elif elementos == 1:
        return print(f"'{names[0]} likes this'")
    elif elementos == 3:
        return print(f"'{names[0]}, {names[1]} and {names[2]} like this'")
    else:
        return print(f"'{names[0]}, {names[1]} and {(elementos-2)} others like this'") if elementos > 2 else print(f"'{names[0]} and {names[1]} like this'")
felo = []
likes(felo)