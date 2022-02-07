import datetime
# Functional bank system using OOP


class Account(object):
    """
    A class to represent an Account.

    ...

    Attributes
    ----------
    first_name : str
        first name of account holder.
    last_name : str
        last name of the account holder.
    age : int
        age of the account holder.
    account_id : int
        Unique ID of the account.
    customer_id : int
        Id of the customer with the account.
    account_type : str
        Type of the account based on the age.
    account_balance : float
        Balance in the account.

    Methods
    -------
    menu():
        prints a menu for the customer.
    balance():
        returns the balance of the account.
    deposit(amount):
        Deposits the given amount in the account.
    transfer(amount, receiver):
        Transfers amount from current account to the receiver.
    withdraw(amount):
        Withdraws the given amount.
    """

    def __init__(self, first_name, last_name, age, account_id, customer_id, account_type, account_balance):
        """
        Constructs all the necessary attributes for the Account object.

        Parameters
        ----------
            first_name : str
                first name of account holder.
            last_name : str
                last name of the account holder.
            age : int
                age of the account holder.
            account_id : int
                Unique ID of the account.
            customer_id : int
                Id of the customer with the account.
            account_type : str
                Type of the account based on the age.
            account_balance : float
                Balance in the account.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.account_id = account_id
        self.customer_id = customer_id
        self.account_type = account_type
        self.account_balance = account_balance

    @staticmethod  # does not receive any arguments
    def menu():
        print("Welcome to THIS Bank!\n"
              "-----------------------\n"
              "1. Create an account\n"
              "2. View transactions and balance of account\n"
              "3. Perform tasks with account\n"
              "4. Delete your account\n"
              "5. Exit\n")
        userinput = int(input("Select an option: "))  # user input required for menu selection
        return userinput


class Customer(object):
    """
    A class to represent a Customer.

    ...

    Attributes
    ----------
    first_name : str
        first name of customer.
    last_name : str
        last name of the customer.
    age : int
        age of the customer.
    cust_id : int
        Id of the customer.
    """

    def __init__(self, first_name, last_name, age, cust_id):
        """
        Constructs all the necessary attributes for the Account object.

        Parameters
        ----------
            first_name : str
                first name of customer.
            last_name : str
                last name of the customer.
            age : int
                age of the customer.
            cust_id : int
                Id of the customer.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.cust_id = cust_id
        
    def __str__(self):
        return f"Customer ID: {self.cust_id}, Name: {self.first_name} {self.last_name}, Age: {self.age}"


class SavingAccount(Account):
    """
    A class to represent a SavingAccount.

    ...

    Attributes
    ----------
    See Parent Class (Account) for Docstring.

    Methods
    -------
    balance():
        returns the balance of the account.
    deposit(amount):
        Deposits the given amount in the account.
    transfer(amount, receiver, lastTransaction=None):
        Transfers amount from current account to the receiver.
    withdraw(amount, lastTransaction=None):
        Withdraws the given amount.
    """

    def __init__(self, first_name, last_name, age, account_id, customer_id, account_type, account_balance):
        """
            Constructs all the attributes for Parent Class.
        """
        super().__init__(first_name, last_name, age, account_id, customer_id, account_type, account_balance)  # function to make Saving Account subclass of class Account

    def balance(self):
        """
        returns the balance of the account.

        Parameters
        ----------
        None

        Returns
        -------
        None
        """
        return self.account_balance

    def deposit(self, amount):
        """
        Adds the given amount in the account balance.

        Parameters
        ----------
        amount : float
            deposit amount

        Returns
        -------
        True
        """
        self.account_balance += amount
        return True

    def transfer(self, amount, receiver, lastTransaction=None):
        """
        Transfer the given amount to the receiver's account..

        Parameters
        ----------
        amount : float
            transfer amount
        receiver: account
            account to transfer the amount
        lastTransaction: list
            last transaction for this account for transfer.

        Returns
        -------
        True, False: True if successful else False
        """
        
        # If a last transaction was passed in the argument
        if lastTransaction:
            # Checking if the transaction was less than a month ago.
            if datetime.datetime.strptime(lastTransaction[6], '%Y-%m-%d %H:%M:%S.%f') >= datetime.datetime.now() - datetime.timedelta(days=30):
                print("Already a transfer this month, cannot transfer")
                return False
        # If the transferring will result in less than 0 balance for this account.
        if (self.account_balance - amount) < 0:
            print("Limit Reached on the Negative Balance, cannot transfer")
            return False
        self.account_balance -= amount
        receiver.account_balance += amount
        return True

    def withdraw(self, amount, lastTransaction=None):
        """
        Withdraw the amount from the account.

        Parameters
        ----------
        amount : float
            transfer amount
        lastTransaction: list
            last transaction for this account for withdraw.

        Returns
        -------
        True, False: True if successful else False
        """
        if lastTransaction:
            # Checking if withdraw occurred from this account in this month.
            if datetime.datetime.strptime(lastTransaction[6], '%Y-%m-%d %H:%M:%S.%f') >= datetime.datetime.now() - datetime.timedelta(days=30):
                print("Already withdrew this month, cannot withdraw")
                return False
        # If not sufficient balance to withdraw.
        if (self.account_balance - amount) < 0:
            print("Limit Reached on the Negative Balance, cannot withdraw")
            return False
        self.account_balance -= amount
        return True

    def __str__(self):
        return f"Account Type: {self.account_type}, Customer Name: {self.first_name} {self.last_name}, Balance: {self.account_balance}"


class CheckingAccount(Account):
    """
    A class to represent a SavingAccount.

    ...

    Attributes
    ----------
    See Parent Class (Account) for Docstring.
    _LIMIT: int
        negative balance allowed.

    Methods
    -------
    balance():
        returns the balance of the account.
    deposit(amount):
        Deposits the given amount in the account.
    transfer(amount, receiver):
        Transfers amount from current account to the receiver.
    withdraw(amount):
        Withdraws the given amount.
    """

    def __init__(self, first_name, last_name, age, account_id, customer_id, account_type, account_balance):
        """
            Constructs all the attributes for Parent Class.
        """
        super().__init__(first_name, last_name, age, account_id, customer_id, account_type, account_balance)  # function to make Checking Account subclass of class Account
        self._LIMIT = -200
        
    def balance(self):
        """
        returns the balance of the account.

        Parameters
        ----------
        None

        Returns
        -------
        None
        """
        return self.account_balance

    def deposit(self, amount):
        """
        Adds the given amount in the account balance.

        Parameters
        ----------
        amount : float
            deposit amount

        Returns
        -------
        True
        """
        self.account_balance += amount
        return True

    def transfer(self, amount, receiver):
        """
        Transfer the given amount to the receiver's account.

        Parameters
        ----------
        amount : float
            transfer amount
        receiver: account
            account to transfer the amount

        Returns
        -------
        True, False: True if successful else False
        """
        
        # checking if transfer will result in balance less than the allowed limit
        if (self.account_balance - amount) < self._LIMIT:
            print("Limit Reached on the Negative Balance, cannot transfer")
            return False
        self.account_balance -= amount
        receiver.account_balance += amount
        return True

    def withdraw(self, amount):
        """
        Withdraw the amount from the account.

        Parameters
        ----------
        amount : float
            transfer amount

        Returns
        -------
        True, False: True if successful else False
        """
        # checking if transfer will result in balance less than the allowed limit
        if (self.account_balance - amount) < self._LIMIT:
            print("Limit Reached on the Negative Balance, cannot withdraw")
            return False
        self.account_balance -= amount
        return True

    def __str__(self):
        return f"Account Type: {self.account_type}, Customer Name: {self.first_name} {self.last_name}, Balance: {self.account_balance}"


CUSTOMER_FILE = 'customers.txt'
ACCOUNTS_FILE = 'accounts.txt'
TRANSACTION_FILE = 'accountsTransactions.txt'

with open(CUSTOMER_FILE, 'a+') as f:
    pass
with open(ACCOUNTS_FILE, 'a+') as f:
    pass
with open(TRANSACTION_FILE, 'a+') as f:
    pass
customers = []
accounts = []
transactions = []

# Reading all the files and adding them to our lists at the start of the program.
with open(CUSTOMER_FILE, 'r') as customerFile:
    for line in customerFile.readlines():
        line = line.strip()
        name, lastName, age, customerID = line.split(',')
        customers.append(Customer(name, lastName, age, customerID))

with open(ACCOUNTS_FILE, 'r') as accountsFile:
    for line in accountsFile.readlines():
        line = line.strip()
        name, lastName, age, accountId, customerID, accountType, account_balance = line.split(',')
        if accountType == 'Savings':
            accounts.append(SavingAccount(name, lastName, age, accountId, customerID, accountType, float(account_balance)))
        else:
            accounts.append(CheckingAccount(name, lastName, age, accountId, customerID, accountType, float(account_balance)))
        
with open(TRANSACTION_FILE, 'r') as transactionsFile:
    for line in transactionsFile.readlines():
        line = line.strip()
        transactionID, accountID, transactionType, customerID, receiverID, amount, time = line.split(',')
        transactions.append([transactionID, accountID, transactionType, customerID, receiverID, amount, time])

currentCustomer = None

# Starting a loop which will run our main program.
while True:
    # Making the customer to login to the system with their id.
    print("Welcome.\n1. New customer.\n2. Old Customer.\n3. Exit.")
    customerInput = int(input('Enter your choice: '))
    if customerInput == 1:  # If new customer, adding them in our data
        print('Please enter your details.')
        name = input("Please enter your first name: ")
        lastName = input("Please enter your last name: ")
        age = int(input("Please enter your age: "))
        id = len(customers) + 1
        customers.append(Customer(name, lastName, age, id))
        customer = customers[-1]
        with open(CUSTOMER_FILE, 'a') as f:
            f.write(f"{customer.first_name},{customer.last_name},{customer.age},{customer.cust_id}\n")  
        print("Your customer ID is " + str(id))
        currentCustomer = customers[-1]
    elif customerInput == 2:  # If an already customer, asking about the id and then moving forward.
        print("Enter you customer ID to login.")
        customerID = input("Customer ID: ")
        foundCustomer = [customer for customer in customers if int(customer.cust_id) == int(customerID)]
        if len(foundCustomer) == 0:
            print(f"No customer found with ID {customerID}")
        else:
            currentCustomer = foundCustomer[0]
    elif customerInput == 3:  # Exit out of the system.
        break
    else:  # Invalid Input.
        print('Wrong Input.')
        
    if not currentCustomer:
        continue
    while True:  # If a customer was found.
        userInput = Account.menu()  # Showing the Accounts menu.
        if userInput == 1:  # If user input 1, creating an account.
            foundCustomer = [account for account in accounts if account.customer_id == currentCustomer.cust_id]
            # If the customer has already an account showing error and going back.
            if len(foundCustomer) > 0:
                print("You already have an account setup.")
                continue
            # Else checking if the customer is 18 or older than 18 years.
            if int(currentCustomer.age) >= 18:
                # Making a CheckingAccount for the customer.
                accountID = len(accounts) + 1
                accounts.append(CheckingAccount(currentCustomer.first_name, currentCustomer.last_name, currentCustomer.age, accountID, currentCustomer.cust_id, "Checking", 0.0))
                account = accounts[-1]
                with open(ACCOUNTS_FILE, 'a') as f:
                    f.write(f"{account.first_name},{account.last_name},{account.age},{account.account_id},{account.customer_id},{account.account_type},{account.account_balance}\n")
                print("A checking account was created.")
            # Else if the customer is older than 14.
            elif int(currentCustomer.age) >= 14:
                # Creating a savings account.
                accountID = len(accounts) + 1
                accounts.append(SavingAccount(currentCustomer.first_name, currentCustomer.last_name, currentCustomer.age, accountID, currentCustomer.cust_id, "Savings", 0.0))
                account = accounts[-1]                
                with open(ACCOUNTS_FILE, 'a') as f:
                    f.write(f"{account.first_name},{account.last_name},{account.age},{account.account_id},{account.customer_id},{account.account_type},{account.account_balance}\n")
                print("A savings account was created.")
            else:
                print("You are too young to create an account.")
                
        elif userInput == 2:  # Showing details of the accounts for the customer.
            openedAccounts = [account for account in accounts if account.customer_id == currentCustomer.cust_id]
            # If there are no accounts for the customer, showing error.
            if len(openedAccounts) == 0:
                print("You have no accounts setup.")
                continue
            currentAccount = openedAccounts[0]
            print(f"{currentAccount.account_type} Account ID; ID {currentAccount.account_id}")
            while True:
                # Asking whether to check for balance or transactions.
                print("Menu.\n1.Balance.\n2.Transactions.\n3.Back.")
                choiceInput = int(input("Enter: "))
                if choiceInput == 1:  # Printing the balance of the account.
                    print("The account balance is: $" + str(currentAccount.account_balance))
                elif choiceInput == 2:  # Printing all the transactions that happened with this account.
                    accountTransactions = [transaction for transaction in transactions if transaction[1] == currentAccount.account_id]
                    print(f"{'Transaction ID': <15}{'Account ID': <11}{'Transaction Type': <20}{'Customer ID': <12}{'Receiver ID': <12}{'Amount': <10}{'Time': <15}")
                    for transaction in accountTransactions:
                        print(f"{transaction[0]: <15}{transaction[1]: <11}{transaction[2]: <20}{transaction[3]: <12}{transaction[4]: <12}{transaction[5]: <10}{transaction[6]: <15}")
                elif choiceInput == 3:
                    break
                else:
                    print("Wrong Input, Please try again.")
        elif userInput == 3:  # Performing operations with account.
            openedAccounts = [account for account in accounts if account.customer_id == currentCustomer.cust_id]
            if len(openedAccounts) == 0:
                print("You have no accounts setup.")
                continue
            currentAccount = openedAccounts[-1]
            while True:  # Asking if the user wants to deposit, withdraw or transfer.
                print("Menu.\n1.Deposit.\n2.Withdraw.\n3.Transfer.\n4.Back.")
                choiceInput = int(input("Enter: "))
                if choiceInput == 1:  # If depositing
                    amount = float(input("Enter the amount to add: "))
                    result = currentAccount.deposit(amount)  # calling the deposit function.
                    if result:  # If successful.
                        print("Transaction completed successfully")
                        transactionID = len(transactions) + 1
                        # Adding the transaction and updating account.
                        transactions.append([transactionID, currentAccount.account_id, "Deposit", currentCustomer.cust_id, 0, amount, str(datetime.datetime.now())])
                        with open(TRANSACTION_FILE, 'a') as f:
                            f.write(",".join([str(x) for x in transactions[-1]]) + "\n")        
                        with open(ACCOUNTS_FILE, 'w') as f:
                            for account in accounts:
                                f.write(f"{account.first_name},{account.last_name},{account.age},{account.account_id},{account.customer_id},{account.account_type},{account.account_balance}\n")
                    else:
                        print("error")
                elif choiceInput == 2:  # If withdraw
                    amount = float(input("Enter the amount to withdraw: "))
                    # If savings account, checking for the last transaction(if it's already been done this month)
                    if currentAccount.account_type == "Savings":
                        lastWithdrawTransaction = [transaction for transaction in transactions if transaction[1] == currentAccount.account_id and transaction[2] == "Withdraw"]
                        if len(lastWithdrawTransaction) == 0:
                            lastWithdrawTransaction = None
                        else:
                            lastWithdrawTransaction = lastWithdrawTransaction[-1]
                        # Calling withdraw function, with the last transaction.
                        result = currentAccount.withdraw(amount, lastWithdrawTransaction)
                    else:  # else if checking account, just withdrawing simply.
                        result = currentAccount.withdraw(amount)
                    if result:
                        # If withdraw successful
                        print("Transaction completed successfully")
                        transactionID = len(transactions) + 1
                        transactions.append([transactionID, currentAccount.account_id, "Withdraw", currentCustomer.cust_id, 0, amount, str(datetime.datetime.now())])
                        with open(TRANSACTION_FILE, 'a') as f:
                            f.write(",".join([str(x) for x in transactions[-1]]) + "\n")     
                        with open(ACCOUNTS_FILE, 'w') as f:
                            for account in accounts:
                                f.write(f"{account.first_name},{account.last_name},{account.age},{account.account_id},{account.customer_id},{account.account_type},{account.account_balance}\n")
                
                elif choiceInput == 3:  # If transferring
                    # Asking for the amount and the account Id to transfer to.
                    amount = float(input("Enter the amount to transfer: "))
                    receiverId = input("Enter the ID of the account to transfer: ")
                    receiver = [account for account in accounts if int(account.account_id) == int(receiverId)]
                    if len(receiver) == 0:
                        print("Wrong ID")
                        continue
                    receiver = receiver[0]
                    # Same as before, if savings, getting last transactions this time for transfer.
                    if currentAccount.account_type == "Savings":
                        lastTransferTransaction = [transaction for transaction in transactions if transaction[1] == currentAccount.account_id and transaction[2] == "Transfer"]
                        if len(lastTransferTransaction) == 0:
                            lastTransferTransaction = None
                        else:
                            lastTransferTransaction = lastTransferTransaction[-1]
                        result = currentAccount.transfer(amount, receiver, lastTransferTransaction)
                    else:
                        result = currentAccount.transfer(amount, receiver)
                    if result:  # If successful, saving the data for accounts and transactions file.
                        print("Transaction completed successfully")
                        transactionID = len(transactions) + 1
                        transactions.append([transactionID, currentAccount.account_id, "Transfer", currentCustomer.cust_id, receiver.account_id, amount, str(datetime.datetime.now())])
                        with open(TRANSACTION_FILE, 'a') as f:
                            f.write(",".join([str(x) for x in transactions[-1]]) + "\n")     
                        with open(ACCOUNTS_FILE, 'w') as f:
                            for account in accounts:
                                f.write(f"{account.first_name},{account.last_name},{account.age},{account.account_id},{account.customer_id},{account.account_type},{account.account_balance}\n")
                elif choiceInput == 4:
                    break
                else:
                    print("Wrong Input, Please try again.")

        elif userInput == 4:  # If deleting account.
            openedAccounts = [account for account in accounts if account.customer_id == currentCustomer.cust_id]
            if len(openedAccounts) == 0:
                print("You have no accounts setup.")
                continue
            currentAccount = openedAccounts[-1]
            print("Account deleted Successfully!")
            # Updating the list and the file.
            accounts = [account for account in accounts if currentAccount.customer_id != account.customer_id]
            with open(ACCOUNTS_FILE, 'w') as f:
                for account in accounts:
                    f.write(f"{account.first_name},{account.last_name},{account.age},{account.account_id},{account.customer_id},{account.account_type},{account.account_balance}\n")
        elif userInput == 5:
            break    
        else:
            print("Wrong Input, Please try again.")    
