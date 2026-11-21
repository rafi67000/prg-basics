import re

content = """
Alice was born on March 12, 1992. Her brother, John, was born on June 5, 1988. They have a mutual friend named Mike, whose phone number is 555-123-4567. In their hometown, which has a population of 1,234 or 1,235 people, a holiday festival is held every year on December 25. Alice works in an office with 30 employees. Her phone number is 555-765-4321.
"""

# formuły REGEX
# r przed stringiem blokuje przetwarzanie znakow specjalnych w stringu
#

date_regex = re.compile(r"\b(?:January|February|March|April|May|June|July|August|September|October|November|December)\s+\d{1,2},\s+\d{4}\b")

phone_regex = re.compile(r"\b\d{3}-\d{3}-\d{4}\b")

comma_regex = re.compile(r"\b\d{1,3}(?:,\d{3})+\b")

capital_regex = re.compile(r"\b[A-Z][a-z]+\b")

whole_values_regex = re.compile(r"\b\d+\b")

# print wszystkich wyrazow spelniajacych formułe REGEX

print(date_regex.findall(content))
print(phone_regex.findall(content))
print(comma_regex.findall(content))
print(capital_regex.findall(content))
print(whole_values_regex.findall(content))
