class BankAccount:
    # don't forget to add some default values for these parameters!
    def __init__(self, int_rate=float(), balance=0): 
        # your code here! (remember, instance attributes go here)
        self.int_rate= int_rate
        self.balance= balance
    def deposit(self, amount):
        self.balance += amount
        print(self.balance)
        return self
    def withdraw(self, amount):
        self.balance -= amount
        print(self.balance)
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
Holder_1.deposit(50).deposit(250).deposit(100).withdraw(200).yield_interest()

Holder_2= BankAccount(1.2,150)
