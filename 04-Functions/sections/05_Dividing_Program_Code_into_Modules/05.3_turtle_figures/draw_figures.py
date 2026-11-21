# Program rysujący kwadrat, trójkąt i prostokąt w dwóch miejscach

import turtle
import figures  # Import własnego modułu figures.py

window = turtle.Screen()  # window – okno rysowania
window.bgcolor("lightgreen")

figures.pen.speed(5)  # Ustawienie szybkości rysowania

# Pierwszy zestaw figur
figures.move_to(-250, 100)
figures.draw_square(80)

figures.move_to(-80, 100)
figures.draw_triangle(90)

figures.move_to(100, 100)
figures.draw_rectangle(120, 70)

# Drugi zestaw figur w innych miejscach
figures.move_to(-250, -120)
figures.draw_square(50)

figures.move_to(-80, -120)
figures.draw_triangle(60)

figures.move_to(100, -120)
figures.draw_rectangle(90, 50)

figures.pen.hideturtle()
window.mainloop()
