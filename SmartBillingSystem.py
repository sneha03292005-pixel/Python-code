print("\n🛒 SMART BILLING SYSTEM 🛒\n")

# Menu with prices
MENU = {
    "milk": 30,
    "bread": 25,
    "eggs": 6,
    "rice": 60,
    "oil": 120,
    "sugar": 40
}

def show_menu():
    print("------ MENU ------")
    for item, price in MENU.items():
        print(f"{item.capitalize()}  - ₹{price}")
    print("------------------\n")

cart = {}

while True:
    show_menu()

    item = input("Enter item name (or 'done' to checkout): ").lower()

    if item == "done":
        break

    if item not in MENU:
        print("❌ Item not available!\n")
        continue

    qty = int(input(f"Enter quantity of {item}: "))

    # Add to cart
    if item in cart:
        cart[item] += qty
    else:
        cart[item] = qty

    print("✔ Added to cart!\n")

# --- Billing Section ---
print("\n🧾 FINAL BILL 🧾")
print("----------------------")

total = 0

for item, qty in cart.items():
    cost = MENU[item] * qty
    total += cost
    print(f"{item.capitalize()} x {qty} = ₹{cost}")

print("----------------------")
print(f"Subtotal: ₹{total}")

# GST 5%
gst = round(total * 0.05)
print(f"GST (5%): ₹{gst}")

grand_total = total + gst
print(f"Total Amount: ₹{grand_total}")

# Payment
paid = int(input("\nEnter amount paid: ₹"))

if paid < grand_total:
    print("❌ Not enough money. Payment failed.")
else:
    print(f"Change to return: ₹{paid - grand_total}")

print("\n🎉 Thank you for shopping! 🎉")
