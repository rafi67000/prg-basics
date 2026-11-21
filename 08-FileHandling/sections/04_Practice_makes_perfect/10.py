with open("clothing.csv", encoding="utf-8") as f: # odczyt z pliku
    next(f)  # pominiecie zbednej linii

    for line in f:
        product_id, name, category, size, color, price, stock = line.strip().split(",") # rozdzielenie linii na dane

        if float(price) < 60 and int(stock) < 40:
            print(f"{name} is in the price range.")
