balance = 1000;
choice = 0;

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
    if(money) < 0:
        print("You have entered an invalid number.")
    else:
        balance  += money
        print("Money added successfully.")
  elif choice == 3:
    money = int(input("Enter the amount you want to withdraw (Must be positive): "))
    if(money) < 0:
        print("You have entered an invalid number.")
    else:
        balance  -= money
        print("Money withdrawn successfully.")
      
  
  else:
      print("Invalid Choice.")