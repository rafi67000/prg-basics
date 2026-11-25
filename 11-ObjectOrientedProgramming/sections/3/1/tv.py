class TV:
    def __init__(self):
        self.is_on = False # stan telewizora

    def turn_on(self):
        self.is_on = True # wlaczenie telewizora

    def turn_off(self):
        self.is_on = False # wylaczenie telewizora

    def show_status(self):
        if self.is_on:
            print("TV is on")
        else:
            print("TV is off")