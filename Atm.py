class Atm:
    def __init__(self, cardNumber, pinNumber):
        self.cardNumber= int(input("Enter your Atm card number: "))
        self.pinNumber= int(input("Enter your Atm Pin number: "))
    
    def start(self):
        print("Started")

    def stop(self):
        print("stopped")

    def cashWithdrawal(self):
        print("Withdrawing....")
        "Amount withdrawn"

    def BalanceEnquiry(self):
        print("Checking")
        "Balance enquired"
        