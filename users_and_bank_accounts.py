# bank account class
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


# user class
class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        # three accounts for user
        self.account = BankAccount(int_rate=0.02, balance=0)
        self.accountChecking = BankAccount(int_rate=0.02, balance=0)
        self.accountSaving = BankAccount(int_rate=0.03, balance=0)
    # display user name and his/her balance
    def display_user_balance(self, accountType):
        if(accountType == 'account'):
            print('User: ' + self.name + ', Account Balance: ', self.account.balance)
        elif(accountType == 'checking'):
            print('User: ' + self.name + ', Checking Balance: ', self.accountChecking.balance)
        elif(accountType == 'saving'):
            print('User: ' + self.name + ', Saving Balance: ', self.accountSaving.balance)
        return self

    # transfer money to another user
    def transfer_money(self, other_user, amount):
        self.account.balance -= amount
        other_user.account.balance += amount
        return self

# create 3 user instances
naruto = User('Naruto Uzumaki', 'naruto@hokage.com')
bunny = User('Bunny Tsukini', 'sailor@moon.com')
jon = User("Jon Snow", "snow@winter.com")

naruto.account.deposit(500).deposit(1000).deposit(1000).withdraw(55)
naruto.display_user_balance('account')
naruto.accountChecking.deposit(100000).withdraw(100)
naruto.display_user_balance('checking')

#manipulate different accounts
bunny.account.deposit(1000).deposit(600).withdraw(10).withdraw(16)
bunny.display_user_balance('account')
bunny.accountSaving.deposit(500000).withdraw(100)
bunny.display_user_balance('saving')

jon.accountChecking.deposit(5000).withdraw(30).withdraw(230).withdraw(40)
jon.display_user_balance('checking')

naruto.transfer_money(jon, 100).display_user_balance('account')
jon.display_user_balance('account')
