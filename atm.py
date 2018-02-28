print("""
************************
AUTOMATIC TELLER MACHINE
************************
""")

print("""Press '1' to Balance
Press '2' to Deposit
Press '3' to Withdraw
Press 'q' to Quit to System
""")

account_balance = 1000

while True:
    action = input("Please choose your transaction:")
    if(action == 'q'):
        print("you're going out the system")
        break
    elif(action == '1'):
        print("Account Balance:\t{}$\n".format(account_balance))
    elif(action =='2'):
        received_money = int(input("\nHow much money can you deposit into the account:"))
        account_balance += received_money
        print("You're current account balance:\t{}$\n".format(account_balance))
    elif(action =='3'):
        withdraw_money = int(input("\nHow much you want to withdraw money:"))
        if(account_balance<withdraw_money):
            print("Insufficient balance")
        else:
            account_balance -= withdraw_money
            print("Amount of money withdrawn: {}$".format(withdraw_money))
            print("You have {}$\n".format(account_balance))