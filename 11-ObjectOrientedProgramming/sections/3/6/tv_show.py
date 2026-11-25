from tv import TV # import klasy TV


def main():
    tv = TV() # stworzenie telewizora
    tv.turn_on()
    tv.show_status()

    tv.volume_up() # zwiekszenie glosnosci
    tv.volume_up()
    tv.show_status()

    tv.volume_down() # zmniejszenie glosnosci
    tv.show_status()

    for i in range(15):
        tv.volume_up() # sprawdzenie limitu 10
    tv.show_status()

    for i in range(15):
        tv.volume_down() # sprawdzenie limitu 0
    tv.show_status()

    tv.turn_off()
    tv.show_status()


if __name__ == "__main__":
    main()
