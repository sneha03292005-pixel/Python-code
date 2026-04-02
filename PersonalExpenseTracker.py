import matplotlib.pyplot as plt

class SmartExpenseTracker:

    def __init__(self):
        self.expenses = {}
        self.income = 0

    def enter_income(self):
        print("\n💰 WELCOME TO SMART EXPENSE TRACKER 💰")
        self.income = float(input("Enter your monthly income (₹): "))
        print(f"\nGreat! Your monthly income is ₹{self.income}\n")

    def add_expenses(self):
        while True:
            category = input("Enter expense category (or 'done' to finish): ").lower()

            if category == "done":
                break

            amount = float(input(f"Enter amount for {category}: ₹"))

            if category in self.expenses:
                self.expenses[category] += amount
            else:
                self.expenses[category] = amount

            self.show_balance()

            more = input("Do you want to add another expense? (yes/no): ").lower()
            if more != "yes":
                break

    def show_balance(self):
        spent = sum(self.expenses.values())
        left = self.income - spent
        print(f"\nTotal Spent So Far: ₹{spent}")
        print(f"Money Left: ₹{left}\n")

    def savings_suggestions(self):
        spent = sum(self.expenses.values())
        left = self.income - spent

        print("\n📌 SMART SAVINGS SUGGESTIONS 📌")
        if left <= 0:
            print("⚠ You have no money left! Try to reduce your expenses next month.")
            return

        sip = left * 0.20
        emergency = left * 0.10
        pure_savings = left * 0.30

        print(f"➡ Put ₹{sip:.2f} (20%) into SIP")
        print(f"➡ Keep ₹{emergency:.2f} (10%) in emergency fund")
        print(f"➡ Save ₹{pure_savings:.2f} (30%) in savings account")

    def spending_advice(self):
        spent = sum(self.expenses.values())

        print("\n📢 SPENDING ADVICE 📢")
        if spent > self.income:
            print("⚠ You overspent your monthly income! Try cutting down expenses.")
        elif spent > (0.8 * self.income):
            print("⚠ You used more than 80% of your income. Be careful.")
        elif spent > (0.5 * self.income):
            print("👍 You are spending moderately.")
        else:
            print("🌟 Excellent! You are saving very well!")

    def leftover_menu(self):
        spent = sum(self.expenses.values())
        left = self.income - spent

        if left <= 0:
            print("\n❗ No money left to manage.")
            return

        # counters for unique categories
        save_count = 1
        invest_count = 1
        pocket_count = 1

        while True:
            print(f"\n💸 You have ₹{left:.2f} left.")
            print("What do you want to do with it?")
            print("1. Save it")
            print("2. Invest it")
            print("3. Keep as pocket money")
            print("4. Exit")

            choice = input("Choose any option (1-4): ").strip()

            if choice == "4":
                print("✔ Exiting leftovers menu.")
                break

            elif choice in ["1", "2", "3"]:
                amount = float(input("Enter how much money you want to use: ₹"))

                if amount > left:
                    print("❌ You don't have that much money left!")
                else:
                    left -= amount
                    print(f"✔ ₹{amount} used successfully!")

                    # unique entry names
                    if choice == "1":
                        category = f"saved_{save_count}"
                        save_count += 1
                    elif choice == "2":
                        category = f"invested_{invest_count}"
                        invest_count += 1
                    elif choice == "3":
                        category = f"pocket_{pocket_count}"
                        pocket_count += 1

                    # store each individually
                    self.expenses[category] = amount

            else:
                print("❌ Invalid input. Please enter 1, 2, 3, or 4.")

            if left <= 0:
                print("\n🎉 You have used all leftover money!")
                break

    def show_expenses(self):
        print("\n------ YOUR EXPENSE SUMMARY ------")
        for cat, amt in self.expenses.items():
            print(f"{cat.capitalize()} : ₹{amt}")
        print("----------------------------------")
        print(f"Total Spent = ₹{sum(self.expenses.values())}")
        print(f"Money Left = ₹{self.income - sum(self.expenses.values())}\n")

    def show_pie_chart(self):
        if not self.expenses:
            print("No expenses to show in chart.")
            return

        labels = list(self.expenses.keys())
        values = list(self.expenses.values())

        plt.figure(figsize=(6, 6))
        plt.pie(values, labels=labels, autopct="%1.1f%%")
        plt.title("Your Expense Distribution")
        plt.show()


# ---------------- MAIN PROGRAM ----------------

tracker = SmartExpenseTracker()

tracker.enter_income()
tracker.add_expenses()
tracker.show_expenses()
tracker.spending_advice()
tracker.savings_suggestions()
tracker.leftover_menu()
tracker.show_pie_chart()

print("\n🌟 THANK YOU FOR USING SMART EXPENSE TRACKER 🌟")
