from random import *
from turtle import *

from freegames import path

car = path('car.gif')
# car = path('./broccolo.gif')
tiles = list(range(32)) * 2
state = {'mark': None, 'taps': 0}
writer = Turtle(visible=False)
hide = [True] * 64


def square(x, y):
    """Draw white square with black outline at (x, y)."""
    up()
    goto(x, y)
    down()
    color('black', 'white')
    begin_fill()
    for count in range(4):
        forward(50)
        left(90)
    end_fill()


def index(x, y):
    """Convert (x, y) coordinates to tiles index."""
    return int((x + 200) // 50 + ((y + 200) // 50) * 8)


def xy(count):
    """Convert tiles count to (x, y) coordinates."""
    return (count % 8) * 50 - 200, (count // 8) * 50 - 200


def tap(x, y):
    """Update mark and hidden tiles based on tap."""
    writer.undo()
    spot = index(x, y)
    print(spot)
    print(xy(spot))
    mark = state['mark']
    writer.write(state['taps'])
    # print(x, y)

    if mark is None or mark == spot or tiles[mark] != tiles[spot]:
        state['mark'] = spot
        state['taps'] += 1
    else:
        hide[spot] = False
        hide[mark] = False
        state['mark'] = None
        state['taps'] += 1


def draw():
    """Draw image and tiles."""
    clear()
    goto(0, 0)
    shape(car)
    stamp()

    for count in range(64):
        if hide[count]:
            x, y = xy(count)
            square(x, y)

    mark = state['mark']

    if mark is not None and hide[mark]:
        x, y = xy(mark)
        up()
        goto(x + 25, y)
        color('black')
        write(tiles[mark], align='center', font=('Arial', 30, 'normal'))

    update()
    ontimer(draw, 100)


shuffle(tiles)
setup(420, 500, 370, 0)
addshape(car)
hideturtle()

writer.goto(150, 220)
writer.write(state['taps'])

tracer(False)
onscreenclick(tap)
draw()
done()