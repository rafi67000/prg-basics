# Zadanie: ocena na podstawie punktów
def pts_to_grade(points):
    # points – liczba zdobytych punktów
    if points >= 18:
        grade = "Excellent"  # grade – ocena końcowa
    elif points >= 14:
        grade = "Good"
    elif points >= 10:
        grade = "Satisfactory"
    else:
        grade = "Fail"
    return grade

test_result = 15  # test_result – przykładowa liczba punktów
final_grade = pts_to_grade(test_result)  # final_grade – ocena za test
print("Points:", test_result, "Grade:", final_grade)
