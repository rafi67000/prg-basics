
# ATM (cash machine) simulator

balance = 1000  # Początkowe saldo konta
pin = '1111'  # Początkowy 4-cyfrowy kod PIN

while True:
    print()
    print("ATM Menu:")
    print("1. Check balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Check PIN")
    print("5. Change PIN")
    print("6. Exit")

    choice = input("Choose an option (1-6): ")
    print()

    if choice == '1':
        print(f"Your current balance is: €{balance}")

    elif choice == '2':
        amount = float(input("Enter the amount to deposit: "))

        if amount > 0:
            balance += amount
            print(f"€{amount} has been deposited. New balance: €{balance}")
        else:
            print("Incorrect amount.")

    elif choice == '3':
        amount = float(input("Enter the amount to withdraw: "))

        if amount > 0 and amount <= balance:
            balance -= amount
            print(f"€{amount} has been withdrawn. New balance: €{balance}")
        else:
            print("Insufficient balance or incorrect amount.")

    elif choice == '4':
        entered_pin = input("Enter your PIN: ")

        if entered_pin == pin:
            print("Correct PIN.")
        else:
            print("Incorrect PIN.")

    elif choice == '5':
        entered_pin = input("Enter your current PIN: ")

        if entered_pin == pin:
            new_pin = input("Enter new 4-digit PIN: ")

            if len(new_pin) == 4 and new_pin.isdigit():
                pin = new_pin
                print("PIN changed successfully.")
            else:
                print("PIN must contain exactly 4 digits.")
        else:
            print("Incorrect current PIN.")

    elif choice == '6':
        print("Exiting... Thank you for using the ATM!")
        break

    else:
        print("Invalid option. Please try again.")
