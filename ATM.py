balance = 1000;
choice = 0;

while choice != 4:
  # Prompt
  print("""
        Welcome to the ATM, enter any of the following numbers:
        1. Check Balance
        2. Deposit Money
        3. Withdraw Money
        3. Exit
  """)
  
  choice = int(input("Your choice: "))
  
  if choice ==1:
      print("Your balance is: " + str(balance))