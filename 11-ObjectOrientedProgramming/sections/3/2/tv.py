class TV:
    def __init__(self):
        self.is_on = False # stan telewizora
        self.channel_no = 1 # numer kanalu

    def turn_on(self):
        self.is_on = True # wlaczenie telewizora

    def turn_off(self):
        self.is_on = False # wylaczenie telewizora

    def show_status(self):
        if self.is_on:
            print(f"TV is on, channel {self.channel_no}")
        else:
            print("TV is off")