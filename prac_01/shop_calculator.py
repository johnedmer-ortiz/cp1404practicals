item_price = 0

num_items = int(input("Number of items: "))
while  num_items < 0:
    print("Invalid number of items!")
    num_items = int(input("Number of items: "))

for i in range(1, num_items+1):
    item_price = item_price + float(input("Price of item: "))

print(f"Total price for {num_items} item(s) is ${item_price:.2f}")
