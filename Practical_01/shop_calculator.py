num_items = int(input("Enter the number of items: "))
total_price = 0
for i in range(num_items):
    item_price = float(input(f"Enter the price of item {i+1}: "))
    total_price += item_price
if total_price > 100:
    total_price *= 0.9
print(f"The total price is ${total_price:.2f}")
