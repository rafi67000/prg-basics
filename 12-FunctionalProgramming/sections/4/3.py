# Program oblicza srednia ocen bez dwojek.

grades = [3.0, 5.0, 2.0, 3.5, 4.0, 4.0, 3.5, 2.0, 4.0, 2.0] # lista ocen

grade_filter = lambda grade: grade != 2.0

positive_grades = list(filter(grade_filter, grades)) # usuniecie dwojek

average = sum(positive_grades) / len(positive_grades) # obliczenie sredniej

print(f"Arithmetic mean for grades {positive_grades} 2.0 is {average:.2f}")
