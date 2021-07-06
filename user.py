# user class
class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account_balance = 0
    # adding the deposit method
    def make_deposit(self, amount):	# takes an argument that is the amount of the deposit
        self.account_balance += amount
        return self

    # withdrawal method
    def make_withdrawal(self, amount):
        self.account_balance -= amount
        return self

    # display user name and his/her balance
    def display_user_balance(self):
        print('User: ' + self.name + ', Balance: ', self.account_balance)
        return self

    # transfer money to another user
    def transfer_money(self, other_user, amount):
        self.account_balance -= amount
        other_user.account_balance += amount
        return self

# create 3 user instances
naruto = User('Naruto Uzumaki', 'naruto@hokage.com')
bunny = User('Bunny Tsukini', 'sailor@moon.com')
jon = User("Jon Snow", "snow@winter.com")

# first user makes 3 deposits, one withdrawal, display balance
# naruto.make_deposit(500)
# naruto.make_deposit(1000)
# naruto.make_deposit(1000)
# naruto.make_withdrawal(55)
# naruto.display_user_balance()
naruto.make_deposit(500).make_deposit(1000).make_deposit(1000).make_withdrawal(55).display_user_balance()

# second user makes 2 deposits and 2 withdrawals, display balance
# bunny.make_deposit(1000)
# bunny.make_deposit(600)
# bunny.make_withdrawal(10)
# bunny.make_withdrawal(16)
# bunny.display_user_balance()
bunny.make_deposit(1000).make_deposit(600).make_withdrawal(10).make_withdrawal(16).display_user_balance()

# # third user makes 1 deposit and 3 withdrawals, display balance
# jon.make_deposit(5000)
# jon.make_withdrawal(30)
# jon.make_withdrawal(230)
# jon.make_withdrawal(40)
# jon.display_user_balance()
jon.make_deposit(5000).make_withdrawal(30).make_withdrawal(230).make_withdrawal(40).display_user_balance()

# # Bonus: first user transfers money to third user, print their balances
# naruto.transfer_money(jon, 100)
# naruto.display_user_balance()
# jon.display_user_balance()
naruto.transfer_money(jon, 100).display_user_balance()
jon.display_user_balance()
