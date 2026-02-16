class BankAccount:
    def __init__(self, name, balance=0):
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print("Deposited successfully")

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print("Withdraw successful")
        else:
            print("Insufficient balance")

    def check_balance(self):
        print(f"Balance: ₹{self.balance}")


account = BankAccount("Sreehari", 1000)

while True:
    print("\n1.Deposit 2.Withdraw 3.Balance 4.Exit")
    choice = input("Choose: ")

    if choice == "1":
        amt = float(input("Amount: "))
        account.deposit(amt)

    elif choice == "2":
        amt = float(input("Amount: "))
        account.withdraw(amt)

    elif choice == "3":
        account.check_balance()

    elif choice == "4":
        break
