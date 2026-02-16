expenses = {}

def add_expense(category, amount):
    if category in expenses:
        expenses[category] += amount
    else:
        expenses[category] = amount

def show_expenses():
    total = 0
    for category, amount in expenses.items():
        print(f"{category}: ₹{amount}")
        total += amount
    print("Total:", total)

while True:
    print("\n1.Add Expense  2.Show  3.Exit")
    choice = input("Choice: ")

    if choice == "1":
        cat = input("Category: ")
        amt = float(input("Amount: "))
        add_expense(cat, amt)

    elif choice == "2":
        show_expenses()

    elif choice == "3":
        break
