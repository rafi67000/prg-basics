# Moduł z funkcjami rysującymi figury za pomocą turtle

import turtle

# pen – obiekt żółwia, którym rysujemy
pen = turtle.Turtle()

def draw_square(length):
    # length – długość boku kwadratu
    for i in range(4):  # i – numer kolejnego boku
        pen.forward(length)
        pen.right(90)

def draw_triangle(length):
    # length – długość boku trójkąta równobocznego
    for i in range(3):  # Trzy boki trójkąta
        pen.forward(length)
        pen.left(120)

def draw_rectangle(length_a, length_b):
    # length_a, length_b – długości dwóch różnych boków prostokąta
    for i in range(2):  # Dwa razy rysujemy parę boków
        pen.forward(length_a)
        pen.right(90)
        pen.forward(length_b)
        pen.right(90)

def move_to(x, y):
    # x, y – współrzędne nowego miejsca rozpoczęcia rysowania
    pen.penup()  # Podniesienie pisaka – przemieszczanie bez rysowania
    pen.goto(x, y)
    pen.pendown()  # Opuszczenie pisaka – ponowne rysowanie
