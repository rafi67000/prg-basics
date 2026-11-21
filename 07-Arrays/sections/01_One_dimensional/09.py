# Znalezienie kategorii z największym wydatkiem
categories = ["Food", "Transport", "Rent", "Entertainment"]
expenses = [500, 150, 1000, 200]

max_index = 0
for i in range(len(expenses)):
    if expenses[i] > expenses[max_index]:
        max_index = i

print("Most expensive category:", categories[max_index])
print("Expense:", expenses[max_index])
