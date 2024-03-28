import classes

test = classes.BankAccount(owner="Jonh", balance=2000)
print(test.owner,test.balance)
test2 = classes.BankAccount.CheckingAccount(withdraw="yestrerday", deposit=102)
print(test2.withdraw,test2.deposit)
test3 = classes.BankAccount.CheckingAccount(withdraw="today", deposit=508)
print(test3.withdraw,test3.deposit)