# Program testujący funkcje z modułu converters

import converters  # Import pliku converters.py z tego samego folderu

print("### Test converters")
print(f"Three meters is {converters.m_to_cm(3)} cm")
print(f"100 cm is {converters.cm_to_m(100)} m")
print(f"10 cm is {converters.cm_to_inches(10):.2f} inches")
print(f"5 feet 8 inches is {converters.feet_inches_to_cm(5, 8):.2f} cm")
