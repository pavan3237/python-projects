class BankAccount:
    def __init__(self, owner, password, balance=0):
        self.owner = owner
        self.__password = password
        self.balance = balance
        self.history = []

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            self.history.append(f"Deposited ₹{amount}")
            print(f"Deposited ₹{amount}. New balance: ₹{self.balance}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            self.history.append(f"Withdrew ₹{amount}")
            print(f"Withdrew ₹{amount}. New balance: ₹{self.balance}")
        else:
            print("Insufficient funds or invalid amount.")

    def check_balance(self):
        print(f"{self.owner}, your balance is ₹{self.balance}")

    def get_history(self):
        print("Transaction History:")
        for transaction in self.history:
            print(transaction)

class Bank:
    def __init__(self):
        self.accounts = {}

    def add_account(self, account):
        self.accounts[account.owner] = account

# Testing the class
account1 = BankAccount("pavan", 123, 1000)
account1.deposit(500)
account1.withdraw(200)
account1.check_balance()
account1.get_history()
