balance = 1000;
choice = 0;
transactions = 0
warning = 0
password = "1234"
check = ""

while(check != password):
    check = input("Please enter the password to login: ")
    if(check != password):
        print("Wrong password please try again.")


while choice != 4:
  # Prompt
  print("""
        Welcome to the ATM, enter any of the following numbers:
        1. Check Balance
        2. Deposit Money
        3. Withdraw Money
        4. Exit
  """)
  
  choice = int(input("Your choice: "))
  
  if choice == 1:
      print("Your balance is: " + str(balance))
      
  elif choice == 2:
    money = int(input("Enter the amount you want to add (Must be positive): "))
    if(money > 0):
        balance  += money
        print("Money added successfully.")
        transactions += 1
    else:
        print("You have entered an invalid number.")
        
  elif choice == 3:
    money = int(input("Enter the amount you want to withdraw (Must be positive): "))
    if(money > 0):
        if(money > balance):
            print("You don't have enough money to withdraw the current amount.")
            warning += 1
            if(warning > 3):
                print("You have failed in your withdrawal too many times. Total transactions: "  + str(transactions))
                break

        else:
            balance  -= money
            print("Money withdrawn successfully.")
            transactions += 1
    else:
        print("You have entered an invalid number.")
            
        
  elif choice == 4:
    print("Program ended. Total transactions: "  + str(transactions))
        
  else:
      print("Invalid Choice.")
      
