#def atm_program():
balance = 0

while True:
    print("\n----- MENU -----")
    print("1. Add Money")
    print("2. Withdraw Money")
    print(" 3. Exit and Show Balance")
    
choice = int(input("Choose an option (1/2/3): "))

if choice == '1':
    
    amount = int(input("Enter amount to add: ₹"))
if amount > 0:
    
    balance += amount
               # print(f"₹{amount} added successfully. Current balance: ₹{balance}")
else:
    print("Enter a valid amount!")

    elif choice == '2':
        amount = int(input("Enter amount to withdraw: ₹"))
    if amount > balance:
        
        print(f"Insufficient balance!") #your current balance is ₹{balance}")
            elif amount <= 0:
                print("Enter a valid amount!")
            else:
                balance -= amount
               # print(f"₹{amount} withdrawn successfully. Current balance: ₹{balance}")

        elif choice == '3':
            print(f"Exiting... Your final balance is ₹{balance}")
            break

        else:
            print("Invalid choice! Please select 1, 2, or 3.")

# Call the function to run the program
#atm_program()
