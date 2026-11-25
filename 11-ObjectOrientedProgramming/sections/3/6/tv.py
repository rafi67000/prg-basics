class TV:
    def __init__(self):
        self.is_on = False # stan telewizora
        self.channel_no = 1 # numer kanalu
        self.channels = [] # lista kanalow
        self.volume = 0 # poziom glosnosci

    def turn_on(self):
        self.is_on = True # wlaczenie telewizora

    def turn_off(self):
        self.is_on = False # wylaczenie telewizora

    def set_channel(self, new_channel_no):
        self.channel_no = new_channel_no # zmiana kanalu

    def set_channels(self, channels_list):
        self.channels = channels_list # ustawienie kanalow

    def show_channels(self):
        print("Channel list:")
        for i in range(len(self.channels)):
            print(f"{i + 1}. {self.channels[i]}")

    def volume_up(self):
        if self.volume < 10:
            self.volume += 1 # zwiekszenie glosnosci

    def volume_down(self):
        if self.volume > 0:
            self.volume -= 1 # zmniejszenie glosnosci

    def show_status(self):
        if self.is_on:
            print(f"TV is on, channel {self.channel_no}, volume {self.volume}")
        else:
            print("TV is off")
