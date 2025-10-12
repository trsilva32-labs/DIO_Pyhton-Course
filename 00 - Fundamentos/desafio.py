"""BASIC BANK SYSTEM (DIO TRAINING)"""
# pylint: disable=invalid-name
MENU = f"""
{'OPTIONS'.center(50, '=')}
[D] Deposit
[W] Withdraw
[S] bank statement
[Q] Quit
{'='.center(50, "=")}
Type your option => """

LIMIT = 500
WITHDRAW_LIMIT = 3
balance = 0
bank_statement = ""
withdraw_count = 0


while True:

    option = input(MENU)

    if option.lower() == "d":
        amount = float(input("How much you will be depositing: "))

        if amount > 0:
            balance += amount
            bank_statement += f"Deposit: ${amount:.2f}\n"

        else:
            print(f"FAIL!!! ${amount:.2f} Amount not valid.")

    elif option.lower() == "w":
        amount = float(input("How much money do you need: "))

        exceeded_amount = amount > balance

        exceeded_limit = amount > LIMIT

        exceeded_withdraw_count = withdraw_count >= WITHDRAW_LIMIT

        if exceeded_amount:
            print("FAIL! NO BALANCE.")

        elif exceeded_limit:
            print("FAIL! Amount Exceeded.")

        elif exceeded_withdraw_count:
            print("FAIL! Exceed Number of Withdraws.")

        elif amount > 0:
            balance -= amount
            bank_statement += f"Withdraw: ${amount:.2f}\n"
            withdraw_count += 1

        else:
            print("FAIL! The amount of ${{amount:.2f}} is not valid.")

    elif option.lower() == "s":
        print(f"\n{'BANK STATEMENT STARTS'.center(50, '=')}")
        print("No account movements identified" if not bank_statement else bank_statement)
        print(f"\nBalance: ${balance:.2f}")
        print(f"\n{'BANK STATEMENT ENDS'.center(50, '=')}")

    elif option.lower() == "q":
        break

    else:
        print("Invalid Option, please try again wiht a valid option")
