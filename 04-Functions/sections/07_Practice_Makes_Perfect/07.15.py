# 15. Sprawdzanie palindromu
def is_palindrome(palindrome):
    # palindrome – tekst sprawdzany od przodu i od tyłu
    return palindrome == palindrome[::-1]  # [::-1] odwraca tekst

print(is_palindrome("radar"))
print(is_palindrome("12-11-21"))
print(is_palindrome("book"))
