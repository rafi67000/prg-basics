#sterowanie oświetleniem w domu
#jeden przełącznik włącza jedną żarówkę a drugi przełącznik włącza dwie żarówki

light_switch1 = False  #pierwszy przełącznik
light_switch2 = False  #drugi przełącznik

bulbs_on = 0  #liczba świecących żarówek

#jeżeli pierwszy przełącznik jest włączony zwiększamy liczbę świecących żarówek o 1
if light_switch1:
    bulbs_on += 1

#jeżeli drugi przełącznik jest włączony zwiększamy liczbę świecących żarówek o 2
if light_switch2:
    bulbs_on += 2

print(f'Number of bulbs on: {bulbs_on}')