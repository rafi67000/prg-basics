
import time

countdown = int(input("Enter the number of seconds to count down: "))

#lista słów odpowiadających ostatnim pięciu sekundom
words = ["one", "two", "three", "four", "five"]

while countdown > 0:
    if countdown <= 5: #if countdown <= 5 – sprawdza, czy zostało maksymalnie 5 sekund
        print(words[countdown - 1])#words[countdown - 1] – pobiera odpowiednie słowo z listy
    else:
        print(countdown)

    countdown -= 1
    time.sleep(1)  #Wait for 1 second

print("Time's up!")
