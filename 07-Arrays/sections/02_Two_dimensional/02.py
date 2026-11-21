# Tygodniowe wydatki: Food, Transport, Utilities
monthly_expenses = [
    [200, 50, 100],
    [180, 60, 110],
    [220, 55, 105],
    [210, 65, 95]
]

# Sumowanie kategorii (kolumn)
food_total = 0
transport_total = 0
utilities_total = 0
for week in monthly_expenses:
    food_total += week[0]
    transport_total += week[1]
    utilities_total += week[2]

# Sumowanie tygodni (wierszy)
week_totals = []
for week in monthly_expenses:
    week_total = 0
    for value in week:
        week_total += value
    week_totals.append(week_total)

# Suma miesięczna
month_total = food_total + transport_total + utilities_total

print("MONTHLY EXPENSES")
print("----------------")
print("Food:", food_total)
print("Transport:", transport_total)
print("Utilities:", utilities_total)
print("Week 1:", week_totals[0])
print("Week 2:", week_totals[1])
print("Week 3:", week_totals[2])
print("Week 4:", week_totals[3])
print("---------------")
print("TOTAL:", month_total)
