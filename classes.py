class BankAccount:
    def __init__(self,balance,owner) -> None:
        self.balance = balance
        self.owner = owner
    class CheckingAccount:
        def __init__(self,withdraw,deposit) -> None:
            self.withdraw = withdraw
            self.deposit = deposit
    class SavingsAccount:
        def __init__(self,withdraw,deposit) -> None:
            self.withdraw = withdraw
            self.deposit = deposit