with open("powers.txt", "w", encoding="utf-8") as f: # odczyt z pliku
    for n in range(1, 101): # od 1 do 100
        line = f"{n},{n**2},{n**3}" # liczba, kwadrat liczby, szescian liczby
        print(line)
        f.write(line + "\n") # zapis w pliku