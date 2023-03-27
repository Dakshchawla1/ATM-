from tkinter import *
# atm code made by daksh and chirag

class ATM:
    def __init__(self, master):
        self.master = master
        self.master.title("ATM Machine")
        self.master.geometry("300x150")

        self.balance = 0

        self.balanceLabel = Label(self.master, text="Balance: $0")
        self.balanceLabel.pack()

        self.withdrawButton = Button(self.master, text="Withdraw", width=10, command=self.withdraw)
        self.withdrawButton.pack(side=LEFT, padx=5)

        self.depositButton = Button(self.master, text="Deposit", width=10, command=self.deposit)
        self.depositButton.pack(side=RIGHT, padx=5)

    def withdraw(self):
        amount = int(input("Enter the you want to  amount to withdraw: "))
        if amount > self.balance:
            print("Insufficient funds!!")
        else:
            self.balance -= amount
            self.balanceLabel.config(text="Balance: ${}".format(self.balance))

    def deposit(self):
        amount = int(input("Enter amount you want to deposit: "))
        self.balance += amount
        self.balanceLabel.config(text="Balance: ${}".format(self.balance))

root = Tk()
atm = ATM(root)
root.mainloop()
