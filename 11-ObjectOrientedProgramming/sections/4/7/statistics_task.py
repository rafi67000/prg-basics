class Statistics:
    def __init__(self):
        self.numbers = [] # lista liczb

    def add_number(self):
        number = float(input("Enter number: ")) # odczyt liczby
        self.numbers.append(number)

    def show_numbers(self):
        print(*self.numbers) # wyswietlenie liczb

    def maximum(self):
        return max(self.numbers) # najwieksza liczba

    def minimum(self):
        return min(self.numbers) # najmniejsza liczba

    def mean(self):
        return sum(self.numbers) / len(self.numbers) # srednia

    def median(self):
        numbers = sorted(self.numbers) # sortowanie liczb
        middle = len(numbers) // 2 # srodek listy
        if len(numbers) % 2 == 0:
            return (numbers[middle - 1] + numbers[middle]) / 2
        return numbers[middle]

    def show_statistics(self):
        print("Minimum:", self.minimum())
        print("Maximum:", self.maximum())
        print("Mean:", self.mean())
        print("Median:", self.median())


stats = Statistics()
for i in range(5):
    stats.add_number() # wczytanie pieciu liczb
stats.show_numbers()
stats.show_statistics()
