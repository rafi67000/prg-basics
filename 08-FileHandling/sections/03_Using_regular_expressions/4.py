import re  # module for regular expressions

# file name with shopping report
email_file = 'report.txt'

# read the content of email
with open(email_file, "r", encoding="utf-8") as file:
    email = file.read()

# regular expression pattern for amounts
pattern = r'€\d+'

# extract numbers from email
amounts = re.findall(pattern, email)

# calculate the total purchases
total = 0

for amount in amounts:
    value = int(amount.replace('€', '')) # konwersja na int
    total += value # sumowanie

# print result
print(f"Total money spent: {total:.2f} €") # .2f - 2 cyfry po przecinku
