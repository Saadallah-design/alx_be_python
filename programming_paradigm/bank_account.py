# Objective: implementing a BankAccount class that encapsulates banking operations.
# The class should support deposit, withdrawal, and balance display.
# Use main_0.py to test the class.
 # -------------------------------
# WHAT IS A CLASS?  
# A class is a blueprint for creating objects. It defines a set of attributes and methods that the created objects will have.
# For example, a car class might have attributes like color and model, and methods like drive and stop.
# And with the car class, you can create multiple car objects, each with its own specific attributes.
# Classes help organize code, promote reusability, and encapsulate data and behavior.
# -------------------------------

class BankAccount:
    # First, we define the class and its constructor
    # use __init__ method to initialize the account with a starting balance
    # Self refers to the current instance of the class itself
    # self is always the first parameter of any method in a class

    def __init__(self, account_balance=0):
        self.account_balance = account_balance
        # print(f"Current account balance: ${self.account_balance}")

    # Method to deposit money into the account
    def deposit(self, amount):
        # Check if the amount is positive
        # if the amount is valid, add it to the account balance
        if amount > 0:
            self.account_balance += amount
            return True
        # early exit if the amount is invalid
        # it returns False back to the caller, signaling that the deposit failed 
        # because of an invalid amount
        return False
    
    # Method to withdraw money from the account
    def withdraw(self, amount):
        # first check if the amount is positive and if there are sufficient funds
        if amount > 0 and amount <= self.account_balance:
            self.account_balance -= amount
            return True
        # early exit if the amount is invalid or insufficient funds
        # it returns False back to the caller, signaling that the withdrawal failed
        return False
    
    # Method to display the current account balance
    def display_balance(self):
        print(f"Current Balance: ${self.account_balance}")