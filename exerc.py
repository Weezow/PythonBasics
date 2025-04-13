total = 0
cart = {}

while True:
    food = input("Enter a product to buy (q to quit): ")
    if food.lower() == "q":
        break
    else:
        price = float(input(f"Enter the price of a {food}: $"))
        try:
            if cart[food]:
                cart[food] += price
        except:
            cart[food] = price

print("--- YOUR CART ---")

for item, price in cart.items():
    print(item, price)
#    print(food)
#    total = total + price
    total += price

print()
print(f"Your total is: ${total}")

with open("./Listing.txt", "a+") as file:
    file.write(f"{cart}"