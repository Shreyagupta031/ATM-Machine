balance = 5000
pin = 1234
entered_pin = int(input("Enter your PIN: "))
if entered_pin == pin:
    while True:
        print("\n----- ATM MENU -----")
        print("1. Check Balance")
        print("2. Withdraw Money")
        print("3. Deposit Money")
        print("4. Exit")
        choice = int(input("Enter your choice: "))
        if choice == 1:
            print("Your balance is:", balance)
        elif choice == 2:
            amount = float(input("Enter withdrawal amount: "))
            if amount <= balance:
                balance -= amount
                print("Withdrawal successful!")
                print("Remaining balance:", balance)
            else:
                print("Insufficient balance!")
        elif choice == 3:
            amount = float(input("Enter deposit amount: "))
            balance += amount
            print("Deposit successful!")
            print("Updated balance:", balance)
        elif choice == 4:
            print("Thank you for using the ATM!")
            break
        else:
            print("Invalid choice!")

else:
    print("Incorrect PIN!")