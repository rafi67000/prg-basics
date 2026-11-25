import random

class Thermometer:
    def __init__(self):
        self.is_on = False # stan termometru
        self.temperature = None # brak pomiaru

    def turn_on(self):
        self.is_on = True # wlaczenie

    def turn_off(self):
        self.is_on = False # wylaczenie

    def measure(self):
        if self.is_on:
            self.temperature = random.randint(340, 420) / 10 # losowa temperatura

    def show_temperature(self):
        if self.is_on and self.temperature is not None:
            if self.temperature >= 37:
                print(f"Temperature: {self.temperature:.1f}C (fever)")
            else:
                print(f"Temperature: {self.temperature:.1f}C")
            if self.temperature >= 41:
                print("CRITICAL TEMPERATURE!!")
