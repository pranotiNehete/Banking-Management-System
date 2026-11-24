# BANKING MANAGEMENT SYSTEM

accounts = {}

def createAccount():
    account_no = int(input("Enter your Account Number: "))
    if account_no in accounts:
        print("Account Already Exists!")
        return
    customer_name = input("Enter your Name: ")
    mobile = input("Enter Mobile Number: ")
    account_type = input("Enter Account Type (Savings/Current): ")
    balance = float(input("Enter Initial Balance: "))

    accounts[account_no] = {
        "name": customer_name,
        "mobile": mobile,
        "type": account_type,
        "balance": balance
    }
    print("Account Created Successfully.")

def viewAllAccounts():
    if len(accounts) == 0:
        print("No Accounts Found!")
        return
    for account_no, data in accounts.items():
        print("Customer Account_no=", account_no)
        print("Customer name=", data["name"])
        print("Customer Mobile=", data["mobile"])
        print("Customer Account_type=", data["type"])
        print("Customer Balance=", data["balance"])
        print("*****************")

def searchAccount():
    account_no = int(input("Enter Account Number to Search: "))
    if account_no in accounts:
        data = accounts[account_no]
        print("Customer Account_no=", account_no)
        print("Customer name=", data["name"])
        print("Customer Mobile=", data["mobile"])
        print("Customer Account_type=", data["type"])
        print("Customer Balance=", data["balance"])
    else:
        print("Account Not Found!")

def depositMoney():
    account_no = int(input("Enter Account Number: "))
    if account_no in accounts:
        amount = float(input("Enter Amount to Deposit: "))
        accounts[account_no]["balance"] = accounts[account_no]["balance"] + amount
        print("Money Deposited Successfully.")
    else:
        print("Account Not Found!")

def withdrawMoney():
    account_no = int(input("Enter Account Number: "))
    if account_no in accounts:
        amount = float(input("Enter Amount to Withdraw: "))
        if amount > accounts[account_no]["balance"]:
            print("Insufficient Balance!")
        else:
            accounts[account_no]["balance"] = accounts[account_no]["balance"] - amount
            print("Amount Withdrawn Successfully.")
    else:
        print("Account Not Found!")

def checkBalance():
    account_no = int(input("Enter Account Number: "))
    if account_no in accounts:
        print("Total Balance=", accounts[account_no]["balance"])
    else:
        print("Account Not Found!")

def updateAccount():
    account_no = int(input("Enter Account Number to Update: "))
    if account_no in accounts:
        new_name = input("Enter New Customer Name: ")
        new_mobile = input("Enter New Mobile Number: ")
        accounts[account_no]["name"] = new_name
        accounts[account_no]["mobile"] = new_mobile
        print("Account Updated Successfully.")
    else:
        print("Account Not Found!")

def deleteAccount():
    account_no = int(input("Enter the Account Number to Delete: "))
    if account_no in accounts:
        del accounts[account_no]
        print("Account Deleted Successfully.")
    else:
        print("Account Not Found!")

def main():
    while True:
        print("\n----------------------------------")
        print("   BANKING MANAGEMENT SYSTEM   ")
        print("------------------------------------")
        print("1. Create Account")
        print("2. View All Accounts")
        print("3. Search Account")
        print("4. Deposit Money")
        print("5. Withdraw Money")
        print("6. Check Balance ")
        print("7. Update Customer Details")
        print("8. Delete Account")
        print("9. Exit")
        print("--------------------------------------")
        choice = int(input("Which operation do you want to perform.."))

        if choice == 1:
            createAccount()
        elif choice == 2:
            viewAllAccounts()
        elif choice == 3:
            searchAccount()
        elif choice == 4:
            depositMoney()
        elif choice == 5:
            withdrawMoney()
        elif choice == 6:
            checkBalance()
        elif choice == 7:
            updateAccount()
        elif choice == 8:
            deleteAccount()
        elif choice == 9:
            print("\nThank you for using the Banking Management System. Goodbye.!")
            break
        else:
            print("INVALID INPUT! Please enter a valid number.")

main()
