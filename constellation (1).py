import turtle
import random

ecran = turtle.Screen()
ecran.title("Mon Projet Constellation")
ecran.bgcolor("#0a0a20")
ecran.setup(width=950, height=750)

ecran.tracer(0)

fond = turtle.Turtle()
fond.hideturtle()
fond.penup()
for i in range(200):
    fond.goto(random.randint(-470, 470), random.randint(-370, 370))
    fond.color("gray")
    fond.dot(random.randint(1, 3))

texte = turtle.Turtle()
texte.hideturtle()
texte.penup()
texte.color("white")
texte.goto(-450, 330)
texte.write("CONTROLES : Flèches = Bouger | Espace = Placer étoile | Entrée = Relier | Suppr = Reset", font=("Arial", 10, "bold"))

ecran.tracer(1)

etoiles = []

turtle.shape("circle")
turtle.shapesize(0.5)
turtle.color("white")
turtle.penup()
turtle.speed(0)

lignes = turtle.Turtle()
lignes.hideturtle()
lignes.penup()
lignes.speed(0)

def bouger_haut():
    turtle.goto(turtle.xcor(), turtle.ycor() + 20)

def bouger_bas():
    turtle.goto(turtle.xcor(), turtle.ycor() - 20)

def bouger_gauche():
    turtle.goto(turtle.xcor() - 20, turtle.ycor())

def bouger_droite():
    turtle.goto(turtle.xcor() + 20, turtle.ycor())

def ajouter_etoile():
    position_actuelle = turtle.position()
    etoiles.append(position_actuelle)
    
    turtle.color("orange")
    turtle.dot(16)
    turtle.color("white")
    turtle.dot(6)

def faire_constellation():
    if len(etoiles) < 2:
        return
        
    lignes.clear()
    lignes.penup()
    lignes.color("cyan")
    lignes.width(2)
    
    depart = etoiles[0]
    lignes.goto(depart[0], depart[1])
    lignes.pendown()
    
    for pt in etoiles:
        lignes.goto(pt[0], pt[1])
        
    lignes.penup()

def effacer_tout():
    global etoiles
    etoiles = []
    lignes.clear()
    turtle.clear()
    turtle.goto(0, 0)

ecran.listen()
ecran.onkey(bouger_haut, "Up")
ecran.onkey(bouger_bas, "Down")
ecran.onkey(bouger_gauche, "Left")
ecran.onkey(bouger_droite, "Right")
ecran.onkey(ajouter_etoile, "space")
ecran.onkey(faire_constellation, "Return")
ecran.onkey(effacer_tout, "Delete")

turtle.done()