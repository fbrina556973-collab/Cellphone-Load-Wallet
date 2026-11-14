

class LoadWallet:

    def __init__(self, owner, number, balance):
        self.owner = owner
        self.number = number
        self.balance = balance

  
    def top_up(self, amount):
        if amount > 0:
            self.balance = self.balance + amount
            print(f"New balance: P{self.balance:.2f}")
        else:
            print("Invalid amount!")

  
    def send_load(self, receiver, amount):
        if amount <= 0:
            print("Invalid amount!")
        elif amount > self.balance:
            print("Insufficient balance!")
        else:
            self.balance = self.balance - amount
            print(f"P{amount:.2f} sent to {receiver}")
            print(f"New balance: P{self.balance:.2f}")


    def send_with_fee(self, receiver, amount):
        fee = 5
        total = amount + fee

        if amount <= 0:
            print("Invalid amount!")
        elif total > self.balance:
            print("Insufficient balance!")
        else:
            self.balance = self.balance - total
            print(f"P{amount:.2f} sent to {receiver}")
            print(f"Service fee: P{fee:.2f}")
            print(f"New balance: P{self.balance:.2f}")

    
    def show_balance(self):
        print("\n----- WALLET INFORMATION -----")
        print(f"Owner         : {self.owner}")
        print(f"Mobile Number : {self.number}")
        print(f"Current Balance: P{self.balance:.2f}")
