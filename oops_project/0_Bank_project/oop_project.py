from bank_account import *

jhony = BankAccount(accountname="Jhony",initialbalance=3000)
manasa = BankAccount(accountname="manasa",initialbalance=5000)
Harshitha_poojary = BankAccount(accountname="Harshitha_poojary",initialbalance=10000)

jhony.get_balance()
manasa.get_balance()
Harshitha_poojary.get_balance() 

jhony.deposit(amount=250)

#exception raising 
Harshitha_poojary.withdraw(amount=15000)
#passing try
Harshitha_poojary.withdraw(amount=100)
#exception raising 
Harshitha_poojary.transfer(amount=15000,account=jhony)
#passing try
Harshitha_poojary.transfer(amount=300,account=jhony)

#instance of the IntrestRewardAccount and it is inherited from BankAccount
harsha = IntrestRewardAccount(accountname="harsha", initialbalance=1000)

harsha.get_balance()

harsha.deposit(amount=100)

harsha.transfer(amount=200, account=Harshitha_poojary)

#instance of the SavingsAccount and it is inherited from IntrestRewardAccount
jimmy = SavingsAccount(initialbalance=500, accountname="jimmy")

jimmy.get_balance()

jimmy.deposit(amount=100)

#try pass
jimmy.withdraw(amount=100)

#Exception raising
jimmy.withdraw(30000)

Harshitha_poojary.transfer(amount=9800,account=harsha)