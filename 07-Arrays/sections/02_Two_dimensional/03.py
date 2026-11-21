# Tygodniowy plan posiłków [śniadanie, obiad, kolacja]
meal_plan = [
    ["Oatmeal", "Grilled Chicken Salad", "Spaghetti"],
    ["Pancakes", "Sandwich", "Steak"],
    ["Smoothie", "Chicken Wrap", "Salmon"],
    ["Eggs", "Pasta", "Soup"],
    ["Toast", "Burrito", "Pizza"],
    ["Cereal", "Salad", "Fish Tacos"],
    ["Bagel", "Rice and Beans", "Stir-fry"]
]

# Zwraca nazwę dnia tygodnia
def weekday(n):
    weekdays = ["Monday", "Tuesday", "Wednesday",
                "Thursday", "Friday", "Saturday", "Sunday"]
    return weekdays[n - 1]

# Zwraca posiłki dla danego dnia jako tekst
def day_meal_plan(meal_plan, day_number):
    meals = meal_plan[day_number - 1]
    return meals[0] + ", " + meals[1] + ", " + meals[2]

# Wyświetlanie całego planu
print("WEEKLY MEAL PLAN")
print("(Breakfast, Lunch, Dinner)")
print("==========================")
for i in range(1, len(meal_plan) + 1):
    print(weekday(i) + ": " + day_meal_plan(meal_plan, i))
