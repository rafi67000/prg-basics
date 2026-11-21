# 6. Minimalna liczba monet 1, 2 i 5 zł
def coins_count(amount_to_pay):
    # amount_to_pay – kwota do zapłaty w pełnych złotych
    count = 0  # count – liczba użytych monet
    count += amount_to_pay // 5  # Najpierw używamy monet 5 zł
    amount_to_pay %= 5
    count += amount_to_pay // 2  # Następnie monety 2 zł
    amount_to_pay %= 2
    count += amount_to_pay  # Pozostała kwota jest pokrywana monetami 1 zł
    return count

print(coins_count(23))
print(coins_count(8))
print(coins_count(2))
print(coins_count(0))
