class Phone:
    def __init__(self, brand):
        self.brand = brand # marka telefonu
        self.battery = 100 # poziom baterii
        self.is_on = False # stan telefonu

    def turn_on(self):
        self.is_on = True # wlaczenie telefonu

    def turn_off(self):
        self.is_on = False # wylaczenie telefonu

    def charge(self):
        self.battery = 100 # naladowanie baterii


samsung = Phone("Samsung") # stworzenie telefonu marki samsung
iphone = Phone("iPhone") # stworzenie telefonu marki apple

iphone.turn_on()
iphone.charge()
iphone.turn_off()

print(iphone.brand)
print(iphone.battery)
print(iphone.is_on)