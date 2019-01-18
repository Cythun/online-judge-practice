class BankAccount(object):
    def __init__(self):
        self.balance = 0
        self.open_account = False

    def get_balance(self):
        if self.open_account:
            return self.balance
        else:
            raise ValueError(".+")

    def open(self):
        if self.open_account:
            raise ValueError(".+")
        else:
            self.open_account = True

    def deposit(self, amount):
        if amount < 0:
            raise ValueError(".+")
        if self.open_account:
            self.balance += amount
        else:
            raise ValueError(".+")


    def withdraw(self, amount):
        if amount < 0:
            raise ValueError(".+")
        if self.open_account:
            if self.balance >= amount:
                self.balance -= amount
            else:
                raise ValueError(".+")
        else:
            raise ValueError(".+")

    def close(self):
        if self.open_account:
            self.balance = 0
            self.open_account = False
        else:
            raise ValueError(".+")

