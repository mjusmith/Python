class BankAccount:
    
    Holders =[]
    def __init__(self, int_rate=float(), balance=0):
        self.int_rate= int_rate
        self.balance= balance

        BankAccount.Holders.append(self)


    @classmethod
    def Get_Info(cls):
        for holder in cls.Holders:
            holder.display_account_info()

    def deposit(self, amount):
        self.balance += amount
        print(self.balance)
        return self
    def withdraw(self, amount):
        if self.balance>amount:
            self.balance -= amount
            print(self.balance)
            return self
        else:
            print("Insufficient Funds")
            return self
    def display_account_info(self):
        print(f"{self.balance}\n{self.int_rate}")
        return self
    def yield_interest(self):
        if self.balance>0:
            self.balance *= self.int_rate
            print(self.balance)
            return self
        else:
            print("Insufficient funds")
            return False
        
Holder_1= BankAccount(1.05,800)
Holder_2= BankAccount(1.2,150)

Holder_1.deposit(50).deposit(250).deposit(100).withdraw(200).yield_interest()

Holder_2.deposit(50).deposit(4000).deposit(80).withdraw(20).deposit(400).withdraw(10000).yield_interest().display_account_info()

BankAccount.Get_Info()