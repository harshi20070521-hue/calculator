name = input("Enter your name: ")
print("Welcome to the ATM,", name)

account_numbers = ["501001", "501002", "501003"]
pins = ["202605", "123456", "654321"]

account_number = input("Enter your account number: ")
pin = input("Enter your PIN: ")

balance = 0.0

while True:
    if account_number in account_numbers:

        index = account_numbers.index(account_number)

        if pin == pins[index]:

            print("Login successful!")
            print("1. Check Balance")
            print("2. Withdraw Money")
            print("3. Deposit Money")
            print("4. Exit")

            choice = input("Enter your choice: ")

            if choice == "1":
                print("Your balance is $", balance)

            elif choice == "2":
                amount = float(input("Enter the amount to withdraw: "))

                if amount <= balance:
                    balance -= amount
                    print("You have withdrawn $", amount)
                    print("Remaining balance: $", balance)
                else:
                    print("Insufficient funds.")

            elif choice == "3":
                amount = float(input("Enter the amount to deposit: "))
                balance += amount
                print("You have deposited $", amount)
                print("Remaining balance: $", balance)

            elif choice == "4":
                print("Thank you for using the ATM. Goodbye!")
                break

            else:
                print("Invalid choice.")

        else:
            print("Invalid PIN.")
            break

    else:
        print("Invalid account number.")
        break      
      
