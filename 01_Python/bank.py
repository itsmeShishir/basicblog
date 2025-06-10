# 4 Pillars and file handling -> app (terminal wala)
import os
import json

from abc import ABC, abstractmethod

# Abstract class -> information
class Account(ABC):
    def __init__(self, account_number, name, balance = 0.0):
        self.account_number = account_number
        self.name = name
        self._balance = balance
    @abstractmethod
    def deposit(self, amount):
        pass

    @abstractmethod
    def withdrawl(self, amount):
        pass

    def get_balance(self):
        return self._balance
    
    # magic methods / dunder methods -> information given print
    def __str__(self):
        return f"Account Number {self.account_number}, the name of account holder is {self.name} and his/her balance is {self._balance}"

# inherit 
class SavaingAccount(Account):
    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
            print(f"Depositing (Saving) : {amount}")
        else:
            print(f"please enter the correct information")

    def withdrawl(self, amount):
        if amount> self._balance:
            self._balance -=amount
            print(f"Withdrawl process of {amount}")
        else:
            print("you have insufficient amount in your account right now")


# poly
class CurrentAccount(Account):
    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
            print(f"Depositing (Current) : {amount}")
        else:
            print(f"please enter the correct information")

    def withdrawl(self, amount):
        if amount> self._balance:
            self._balance -=amount
            print(f"Withdrawl process of {amount}")
        else:
            print("you have insufficient amount in your account right now")

# file handling and Bank System
class BankSystem:
    def __init__(self, filename = "account.json"):
        self.filename = filename
        self.accounts = {}
        self.load_accounts()

    def create_account(self, account_type, account_number, name, initial_balance = 0.0 ):
            if account_number in self.accounts:
                print("Account already exists")
                return
            
            if account_type.lower() == "saving":
                self.accounts[account_number] = SavaingAccount(account_number, name, initial_balance)

            if account_type.lower() =="current":
                self.accounts[account_number] = CurrentAccount(account_number, name, initial_balance)
            else:
                print("none of the above ")
                return 
            self.save_account()
            print(f"{account_type.capitalize()} account created for {name}")

    def get_account(self, account_number):
            return self.accounts.get(account_number , None)
        
    def save_account(self):
            data = {
                acc_num:{
                    "type": acc.__class__.__name__, 
                    "name": acc.name, 
                    "balance": acc.get_balance()
                }
                for acc_num, acc in self.accounts.items()
            } 
            with open(self.filename, "w") as f:
                json.dump(data, f)

    def load_accounts(self):
            if not os.path.exists(self.filename):
                return
            with open(self.filename, "r") as f:
                data = json.load()
            for acc_num , details in data.items():
                acc_type = details["type"]
                if acc_type == "SavingAccount":
                    self.accounts[acc_num] = SavaingAccount(acc_num, details['name'], details['balance'])
                elif acc_type == "CurrentAccount":
                    self.accounts[acc_num] = CurrentAccount(acc_num, details['name'], details['balance'])
                

# Tesing the above class
# while loop 
if __name__ == "__main__":
    bank = BankSystem()

    while True:
        print("\n=== Welcome to MeroBank ===")
        print("1. Create Account")
        print("2. Deposite")
        print("3. Withdraw")
        print("4. Check Balance")
        print("5. Exit")           

        choices = input("Select Options: ")
        if choices =="1":
            acc_type = input("enter account Type (saving/current): ")
            name = input("enter your Full name: ")
            acct_no = input("enter your account number as you prefer ")
            balance = float(input("enter you balance account: "))
            bank.create_account(acc_type, acct_no, name, balance)

        elif choices == "2": 
            acc_no = input("enter your account number: ")
            acc = bank.get_account(acc_no)

            if acc:
                amount = float(input("enter amount to deposite: "))
                acc.deposit(amount)
                bank.save_account()
            else:
                print("Account not found ")
        elif choices == "3":
            acc_no = input("enter your account number: ")
            acc = bank.get_account(acc_no)
            if acc:
                amount = float(input("enter amount to withdraw: "))
                acc.withdrawl(amount)
                bank.save_account()
            else:
                print("Account not found ")

        elif choices == "4":
            acc_no = input("enter your account number: ")
            acc = bank.get_account(acc_no)
            if acc:
                print(acc)
            else:
                print("Account not found ")

        elif choices == "5":
            print("Thank you for using MeroBank")
            break

        else:
            print("Invalid choice")

        



