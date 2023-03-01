import turtle


riley=turtle.Turtle()
riley.width(5)
riley.speed(0)

def draw_star(color):
    for side in range(5):
        riley.forward(100)
        riley.right(144)
        riley.color(color)

def mood_star(x):
    if x=="happy":
        draw_star("pink")
    elif x=="sad":
        draw_star("blue")
    elif x=="sleepy":
        draw_star("green")
    else:
        draw_star("red")

mood_star("sad")
