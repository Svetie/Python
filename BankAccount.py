class BankAccount:
    all_instances = []
    def __init__(self, int_rate, balance=0):
        self.int_rate = int_rate
        self.balance = balance
        BankAccount.all_instances.append(self)
    def deposit(self, amount):
        self.balance += amount
        return self
    def withdraw(self, amount):
        self.balance -= amount
        return self
    def display_account_info(self):
        print('Rate: ', self.int_rate, 'Balance: ', self.balance)
        return self
    def yield_interest(self):
        self.balance = self.balance + self.balance * self.int_rate
        return self
    @classmethod
    def all_the_instances(cls):
        for account in cls.all_instances:
            account.display_account_info()


account1 = BankAccount(0.01, 1000)
account1.display_account_info()
account2 = BankAccount(0.02)
account2.display_account_info()

# account 1
account1.deposit(400).deposit(1000).deposit(500).withdraw(100).yield_interest().display_account_info()

# account 2
account2.deposit(2000).deposit(2000).withdraw(50).withdraw(50).withdraw(50).withdraw(50).yield_interest().display_account_info()

# print all instances of a Bank Account's info
BankAccount.all_the_instances()
