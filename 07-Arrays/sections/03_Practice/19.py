# Użycie funkcji z modułu MyArrays
import MyArrays

numbers = [7, 3, 8, 5, 2]

print("Numbers:", end=" ")
for number in numbers:
    print(number, end=",")
print()
print("Second largest number:", MyArrays.second_largest(numbers))
print("Difference between largest and smallest:", MyArrays.difference_max_min(numbers))
print("Median:", MyArrays.median(numbers))
print("Smallest and largest number:", MyArrays.smallest_largest(numbers))
print("Numbers as a string:", MyArrays.array_to_string(numbers))
