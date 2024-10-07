class ATM:
    def __init__(self, balance=0):
        self.balance = balance

    def check_balance(self):
        print(f"\nYour current balance is: ${self.balance:.2f}")

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"\nYou've successfully deposited ${amount:.2f}.")
            self.check_balance()
        else:
            print("\nInvalid deposit amount. Please try again.")

    def withdraw(self, amount):
        if amount > 0:
            if amount <= self.balance:
                self.balance -= amount
                print(f"\nYou've successfully withdrawn ${amount:.2f}.")
                self.check_balance()
            else:
                print("\nInsufficient funds. Please try again.")
        else:
            print("\nInvalid withdrawal amount. Please try again.")

    def exit(self):
        print("\nThank you for using the ATM. Goodbye!")
        return False

def atm_interface():
    atm = ATM(balance=1000)
    while True:
        print("\nATM Menu:")
        print("1. Check Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Exit")
        
        choice = input("\nEnter your choice (1-4): ")
        
        if choice == '1':
            atm.check_balance()
        elif choice == '2':
            try:
                amount = float(input("Enter the amount to deposit: "))
                atm.deposit(amount)
            except ValueError:
                print("\nInvalid input. Please enter a valid number.")
        elif choice == '3':
            try:
                amount = float(input("Enter the amount to withdraw: "))
                atm.withdraw(amount)
            except ValueError:
                print("\nInvalid input. Please enter a valid number.")
        elif choice == '4':
            if not atm.exit():
                break
        else:
            print("\nInvalid choice. Please try again.")

atm_interface()
