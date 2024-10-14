#Evan McCabe ProficiencyTest: What is happening?

#Functions for the initial bank account, and for the different ways the user can interact with the program.
class BankAccount:
    #The initial state of the accounts(not money in them yet):
    def __init__(self, account_number, balance=0):
        self.account_number = account_number
        self.balance = balance

    #Function for letting the user add money to their account:
    def deposit(self, amount):
        #Make sure the user does not try to deposit nothing:
        if amount > 0:
            #Add the desired amount to the account:
            self.balance += amount
            return True
        return False

    #Function for letting the user take money out of their account:
    def withdraw(self, amount):
        #Make sure the user does not try to remove nothing, or take out more money than they have:
        if 0 < amount <= self.balance:
            #Withdraw the desired amount from the account:
            self.balance -= amount
            return True
        return False

    #Function to allow the user to check how much money is in their account:
    def get_balance(self):
        #Return the amount of money in the selected account:
        return self.balance

#The function that allows a user to make a new account:
def create_account():
    #Allow the user to choose their account number, or which account they're creating:
    account_number = input("Enter account number: ")
    #Allow the user to set how much money they have initially:
    initial_balance = float(input("Enter initial balance: "))
    #Return the account's number and how much money is in it:
    return BankAccount(account_number, initial_balance)

# The main function in the program. Allows the user to interact and create an account,
# withdraw money, deposit money, check their balance, or exit:
def main():
    #Initialize the accounts to be empty at the beginning of the program:
    accounts = {}
    #Allow the user to interact with the accounts and tell them what they can do:
    while True:
        print("\n1. Create Account")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Check Balance")
        print("5. Exit")
        
        #Let the user pick what they want to do:
        choice = input("Enter your choice (1-5): ")
        
        #If the user picks 1(create account):
        if choice == '1':
            #Make a new account(returned values from the create_account() function):
            account = create_account()
            #Set the account to the one the user created:
            accounts[account.account_number] = account
            #Tell the user that heir account has been created:
            print(f"Account {account.account_number} created successfully!")
        
        #If the uesr picks 2, 3, or 4(Deposit, withdraw, or check balance):
        elif choice in ['2', '3', '4']:
            #Ask the user which account they are acting upon:
            account_number = input("Enter account number: ")
            #Make sure the user actually picks one of the existing accounts:
            if account_number in accounts:
                #Set the account to the one the user picked:
                account = accounts[account_number]
                #If the user picked 2 specifically(deposit):
                if choice == '2':
                    #Set the amount added to the account to what the user desires(and format the value correctly):
                    amount = float(input("Enter deposit amount: "))
                    #Make sure the user makes a valid input amount:
                    if account.deposit(amount):
                        #Tell the user they have successfully deposited money into their account:
                        print(f"Deposited ${amount:.2f} successfully!")
                    #If the user does not make a valid input:
                    else:
                        print("Invalid deposit amount.")
                #If the user picks 3 specifically(withdraw):
                elif choice == '3':
                    #Set the amount the user wants to withdraw from their account:
                    amount = float(input("Enter withdrawal amount: "))
                    #If the user makes a valid input:
                    if account.withdraw(amount):
                        #Tell the user they have successfully withdrawn money from their account:
                        print(f"Withdrawn ${amount:.2f} successfully!")
                    #If the user does not make a valid input(or tries to withdraw more money than they have):
                    else:
                        print("Invalid withdrawal amount or insufficient funds.")
                else:
                    print(f"Current balance: ${account.get_balance():.2f}")
            #If the user chooses an account that does not exist:
            else:
                print("Account not found.")
        
        #If the user picks 5(exit):
        elif choice == '5':
            print("Thank you for using our banking system. Goodbye!")
            #End the program:
            break
        
        #If the user enters an invalid input:
        else:
            print("Invalid choice. Please try again.")

#If the user is on the main page of the program, said program will run:
if __name__ == "__main__":
    main()