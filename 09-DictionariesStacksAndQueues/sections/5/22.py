import json

# Pobranie danych produktu
product = {}
product['name'] = input('Name: ')
# Cenę zamieniamy na liczbę i zaokrąglamy
product['price'] = round(float(input('Price: ').replace(',', '.')), 2)
# Odpowiedź yes oznacza True, pozostałe False
product['paid'] = input('Paid (yes/no): ').strip().lower() == 'yes'

# Zapisanie produktu do pliku
with open('product.json', 'w', encoding='utf-8') as file:
    json.dump(product, file, indent=4, ensure_ascii=False)

print('Saved to product.json')
