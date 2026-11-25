from tv import TV # import klasy TV


def main():
    tv = TV() # stworzenie telewizora
    tv.show_status()
    tv.turn_on() # wlaczenie
    tv.show_status()
    tv.show_channels() # wyswietlenie pustej listy
    tv.set_channels(["TVP1", "TVP2", "Polsat", "TVN", "Filmbox", "Discovery"])
    tv.show_channels() # wyswietlenie kanalow
    tv.show_status()
    tv.turn_off() # wylaczenie


if __name__ == "__main__":
    main()
