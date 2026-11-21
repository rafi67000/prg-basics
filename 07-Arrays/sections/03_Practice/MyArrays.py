# Moduł funkcji do działania na listach liczb

def second_largest(array):
    # Sortujemy kopię listy i wybieramy drugi element od końca
    sorted_array = array.copy()
    n = len(sorted_array)
    for i in range(n):
        for j in range(n - i - 1):
            if sorted_array[j] > sorted_array[j + 1]:
                temp = sorted_array[j]
                sorted_array[j] = sorted_array[j + 1]
                sorted_array[j + 1] = temp
    return sorted_array[n - 2]

def difference_max_min(array):
    # Szukanie największej i najmniejszej wartości
    minimum = array[0]
    maximum = array[0]
    for value in array:
        if value < minimum:
            minimum = value
        if value > maximum:
            maximum = value
    return maximum - minimum

def median(array):
    # Sortowanie kopii i wybieranie środkowego elementu
    sorted_array = array.copy()
    n = len(sorted_array)
    for i in range(n):
        for j in range(n - i - 1):
            if sorted_array[j] > sorted_array[j + 1]:
                temp = sorted_array[j]
                sorted_array[j] = sorted_array[j + 1]
                sorted_array[j + 1] = temp
    if n % 2 == 1:
        return sorted_array[n // 2]
    else:
        return (sorted_array[n // 2 - 1] + sorted_array[n // 2]) / 2

def smallest_largest(array):
    # Zwracanie listy: minimum i maksimum
    minimum = array[0]
    maximum = array[0]
    for value in array:
        if value < minimum:
            minimum = value
        if value > maximum:
            maximum = value
    return [minimum, maximum]

def array_to_string(array):
    # Łączenie elementów w tekst oddzielony myślnikami
    result = ""
    for i in range(len(array)):
        result += str(array[i])
        if i < len(array) - 1:
            result += "-"
    return result
