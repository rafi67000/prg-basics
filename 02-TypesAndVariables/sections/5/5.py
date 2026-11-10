price = float(input("Enter price: "))
discount = int(input("Enter discount in percent: "))

final_price =  price * (1 - discount / 100)

print("""
Product price: %.2f
Discounted price: %.2f
Discount in %%: %d
Reduction amount: %.2f
""" % (price, final_price, discount, price - final_price))