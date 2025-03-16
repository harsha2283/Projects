
class BalanceException(Exception):
    pass

class BankAccount:

    def __init__(self, initialbalance, accountname):
        self.balance = initialbalance
        self.name = accountname
        print(f"#Account creation#\nAccount: '{self.name}' created.\nBalance=  ${self.balance:.2f}")

    def get_balance(self):
        print(f"#Balance of {self.name}#\nAccount: '{self.name}'\nBalance=  ${self.balance:.2f}\n")

    def deposit(self, amount):
        self.balance = self.balance + amount
        print(f"#Deposit#\n#--Amount is Deposited into {self.name}'s account--#" )
        self.get_balance()
    
    def viabletransaction(self, amount):
        if self.balance >= amount:
            return
        else:
            raise BalanceException(f"Sorry the account '{self.name}' has a balance of ${self.balance}")
    
    def withdraw(self, amount):
        try:
            self.viabletransaction(amount)
            self.balance = self.balance - amount
            print("#Withdraw#\nWithdraw is complete.")
            self.get_balance()
        except BalanceException as error:
            print(f"\nWithdraw is interrupted {error}")

    def transfer(self, amount, account):
        try:
            print('#Transaction#\nstart*****\n\nBegining to transfer...🚀')
            self.viabletransaction(amount)
            self.withdraw(amount)
            account.deposit(amount)
            print('Transfer is complete ✅\n\n*******end')
        except BalanceException as error:
            print(f'Transaction is interrupted "❌"\n{error}')

class IntrestRewardAccount(BankAccount):

    def deposit(self, amount):
        self.balance = self.balance + (amount * 1.05)
        print("#Deposit - IntrestRewardAccount#\nDeposit Complete ✅")
        self.get_balance()

class SavingsAccount(IntrestRewardAccount):

    def __init__(self, initialbalance, accountname):
        super().__init__(initialbalance, accountname)
        self.fee = 5

    def withdraw(self, amount):
        try:
            self.viabletransaction(amount)
            self.balance = self.balance - (amount + self.fee)
            print("#Withdraw - SavingsAccount#\nWithdraw is complete")
            self.get_balance()
        except BalanceException as error:
            print(f"Withdraw is interrupted ❌ {error}")
