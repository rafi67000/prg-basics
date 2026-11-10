amount = float(input("Enter the amount: "))
tax_rate = 23

print("""
Amount: %.2f
TAX (23%%): %.2f
""" % (amount, amount * 1.23 - amount))