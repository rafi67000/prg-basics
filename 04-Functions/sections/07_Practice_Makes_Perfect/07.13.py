# 13. Wykrywanie co najmniej 3 osób w pomieszczeniu
def detector(detector_data):
    # detector_data – ciąg znaków + (wejście) i - (wyjście)
    people = 0  # people – aktualna liczba osób w pomieszczeniu
    for sign in detector_data:
        if sign == "+":
            people += 1
        elif sign == "-":
            people -= 1
        if people >= 3:
            return True
    return False

print(detector("+-+++-+---"))
print(detector("+-+-+-+-"))
print(detector("+-++-+--"))
print(detector("+-++-++-+---"))
