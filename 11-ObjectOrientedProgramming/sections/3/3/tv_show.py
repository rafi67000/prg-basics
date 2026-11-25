from tv import TV # import klasy TV


def main():
    tv = TV() # stworzenie telewizora
    tv.show_status() # wyswietlenie stanu
    tv.turn_on() # wlaczenie
    tv.show_status()
    tv.set_channel(5) # zmiana kanalu na 5
    tv.show_status()
    tv.turn_off() # wylaczenie
    tv.show_status()


if __name__ == "__main__":
    main()
