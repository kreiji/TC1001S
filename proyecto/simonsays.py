"""Simon Says"""

'''Maria Carelia Ibarra Vasquez, Jesus Francisco Fong Ruiz, Santiago Ramirez Enriquez
A01251463, A01254062
Herramientas computacionales: el arte de la programacion TC1001S.201
13 de mayo del 2022'''

from csv import writer
from random import choice
from time import sleep
from turtle import *
from playsound import playsound
from random import randrange

from freegames import floor, square, vector

#Colores diferentes en cada juego - Santiago Ramírez
colorarray = ['red','blue','yellow','green','orange','blue violet','white','grey'] #Arrays con los colores claros y oscuros
darkcolorarray = ['dark red', 'dark blue', 'khaki', 'dark green','dark orange', 'dark violet', 'light gray' , 'dim grey']

panel1color = randrange(0,8) #Selecciona el indice del color al azar para cada panel
panel2color = randrange(0,8)
panel3color = randrange(0,8) #Luego se usan estos indices para seleccionar los colores del
panel4color = randrange(0,8) #array en tiles y grid()


state = {'rounds': 0}
writer = Turtle(visible=False)
pattern = []
guesses = []
tiles = {
    vector(0, 0): (colorarray[panel1color], darkcolorarray[panel1color], 'sounds/bonk.mp3'),
    vector(0, -200): (colorarray[panel2color], darkcolorarray[panel2color], 'sounds/hi.mp3'),
    vector(-200, 0): (colorarray[panel3color], darkcolorarray[panel3color], 'sounds/oof.mp3'),
    vector(-200, -200): (colorarray[panel4color], darkcolorarray[panel4color], 'sounds/boing.mp3'),
}

'''Carelia: Cada vector tiene dos colores (uno cuando le das clic y otro para cuando no esta activo) y un string que contiene el nombre del archivo del audio que suena cuando le das clic'''

def grid():
    """Draw grid of tiles."""
    #Dibujar los 4 rectangulos con los colores seleccionados al inicio
    square(0, 0, 200, darkcolorarray[panel1color])
    square(0, -200, 200, darkcolorarray[panel2color])
    square(-200, 0, 200, darkcolorarray[panel3color])
    square(-200, -200, 200, darkcolorarray[panel4color])
    update()


def flash(tile):
    """Flash tile in grid. Sonido - Carelia Ibarra"""

    '''Declaramos glow al primer color en el vector, dark al segundo color, y sound a la string con el nombre del archivo'''
    glow, dark, sound = tiles[tile]
    square(tile.x, tile.y, 200, glow)  #Hace que brille el cuadrado
    update()

    '''Se toma sound y lo ponemos en la funcion playsound para poner el sonido'''
    playsound(sound)
    sleep(0.3)
    
    square(tile.x, tile.y, 200, dark) #Hace que el cuadrado vuelva a estar oscuro
    update()
    sleep(0.3)


def grow():
    """Grow pattern and flash tiles."""
    tile = choice(list(tiles))
    pattern.append(tile)

    for tile in pattern:
        flash(tile)

    print('Pattern length:', len(pattern))
    guesses.clear()

"""Jesus Fong, Contador de rondas"""
def tap(x, y):
    """Respond to screen tap."""
    writer.undo()
    writer.write(len(pattern), font=(20)) 
    """En esta seccion de def tap nos permite agregar un contador de rondas al juego"""
    
    onscreenclick(None)
    x = floor(x, 200)
    y = floor(y, 200)
    tile = vector(x, y)
    index = len(guesses) 

    """Si el jugador presiona el cuadro incorrecto, sale un mensaje de game over, pasan 5 segundos y el juego se cierra"""
    if tile != pattern[index]:
        writer.goto(-50, 0)
        writer.write("GAME OVER", font=(200))
        sleep(5)
        exit()

    """Manda el cuadro seleccionado al array guesses y se manda a la funcion flash"""
    guesses.append(tile)
    flash(tile)

    """Si el jugador selecciono los cuadros en el orden correcto, se llama a la funcion grow"""
    if len(guesses) == len(pattern):
        grow()

    onscreenclick(tap)


def start(x, y):
    """Start game."""
    grow()
    onscreenclick(tap)


setup(420, 500, 370, 0) 
"""Crea la ventana con dimensiones de 420 x 500"""
hideturtle()
tracer(False)
writer.goto(150, 220)
writer.write(len(pattern), font=(20))
grid()
onscreenclick(start)
done()