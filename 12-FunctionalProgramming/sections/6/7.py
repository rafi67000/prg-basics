# Program oblicza punkty zawodnikow w skokach narciarskich.

scores = [
    (17, 15, 16, 17, 15),
    (16, 18, 19, 17, 19),
    (19, 15, 15, 19, 18),
    (18, 17, 19, 15, 16)
] # oceny sedziow

# Suma z odjeciem skrajnych ocen
sum_without_edge_numbers = lambda x: sum(x) - min(x) - max(x)

result = list(map(sum_without_edge_numbers, scores)) # suma bez skrajnych ocen

print(result) # wyswietlenie punktow
