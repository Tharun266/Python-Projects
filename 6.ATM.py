class ATM:
    def __init__(self):
        self.balance = 0.0

    def check_balance(self):
        print(f"Your current balance is: ${self.balance:.2f}")

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Successfully deposited ${amount:.2f}")
        else:
            print("Deposit amount must be positive")

    def withdraw(self, amount):
        if amount > 0:
            if amount <= self.balance:
                self.balance -= amount
                print(f"Successfully withdrew ${amount:.2f}")
            else:
                print("Insufficient funds")
        else:
            print("Withdrawal amount must be positive")

atm = ATM()

while True:
    print("\nATM Menu:")
    print("1. Check Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Exit")
    
    choice = input("Choose an option: ")
    
    if choice == '1':
        atm.check_balance()
    elif choice == '2':
        try:
            amount = float(input("Enter amount to deposit: "))
            atm.deposit(amount)
        except ValueError:
            print("Please enter a valid number.")
    elif choice == '3':
        try:
            amount = float(input("Enter amount to withdraw: "))
            atm.withdraw(amount)
        except ValueError:
            print("Please enter a valid number.")
    elif choice == '4':
        print("Thank you for using the ATM. Goodbye!")
        break
    else:
        print("Invalid option, please choose a valid option")

