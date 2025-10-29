"""BanK System (Using Functions)"""
# pylint: disable=invalid-name
import textwrap


def menu():
    """Menu Method"""
    MENU = """\n
    ================ MENU ================
    [d]\tDeposit
    [w]\tWithdraw
    [s]\tStatement
    [na]\tNew Accont
    [al]\tAccounts List
    [nu]\tNew User
    [q]\tQuit
    => """
    return input(textwrap.dedent(MENU))


def deposit(balance, amount, statement, /):
    """Deposit Method"""
    if amount > 0:
        balance += amount
        statement += f"Deposit:\t$ {amount:.2f}\n"
        print("\n=== Successful Deposit! ===")
    else:
        print("\n@@@ Failed! Invalid amount. @@@")

    return balance, statement


def withdraw(*, balance, amount, statement, limit, withdraw_count, withdraw_count_limit):
    """Withdraw Method"""
    exceeded_balance = amount > balance
    exceeded_amount_limit = amount > limit
    exceeded_withdraw_count_limit = withdraw_count >= withdraw_count_limit

    if exceeded_balance:
        print("\n@@@ Failed! Insuficient balance. @@@")
    elif exceeded_amount_limit:
        print("\n@@@ Failed! Exceded amount limit. @@@")
    elif exceeded_withdraw_count_limit:
        print("\n@@@ Failed! Number of withdraws exceeded. @@@")
    elif amount > 0:
        balance -= amount
        statement += f"Saque:\t\t$ {amount:.2f}\n"
        withdraw_count += 1
        print("\n=== Operation Succeded ! ===")

    else:
        print("\n@@@ Failed! Invalid Amount. @@@")

    return balance, statement


def show_statement(balance, /, *, statement):
    """Statement Method"""
    print("\n================ STATEMENT ================")
    print("No Transactions found" if not statement else statement)
    print(f"\nBalance:\t\t$ {balance:.2f}")
    print("==========================================")


def create_user(users):
    """Create a User Method"""
    ssn = input("Input you SSN (Social Security Number): ")
    user = filter_user(ssn, users)

    if user:
        print("\n@@@ SSN altready exists! @@@")
        return

    name = input("Input you name: ")
    dob = input("Input your Birthday Date(aaaa-mm-dd): ")
    address = input("input your address (street/avenue, number - city/state): ")

    users.append({"name": name, "dob": dob, "ssn": ssn, "address": address})

    print("=== Successfully Created! ===")


def filter_user(ssn, users):
    """Filter User Method"""
    filtered_users = [user for user in users if user["ssn"] == ssn]
    return filtered_users[0] if filtered_users else None


def create_account(branch, account_number, users):
    """Create Account Method"""
    ssn = input("Provide your SSN: ")
    user = filter_user(ssn, users)

    if user:
        print("\n=== Account Successfully created! ===")
        return {"branch": branch, "account_number": account_number, "user": user}

    print("\n@@@ User not found! @@@")


def list_accounts(accounts):
    """List Account Method"""
    for account in accounts:
        linha = f"""\
            Branch:\t{account['branch']}
            Account Number:\t\t{account['account_number']}
            Individual Name:\t{account['user']['name']}
        """
        print("=" * 100)
        print(textwrap.dedent(linha))


def main():
    """Main Method"""
    WITHDRAW_COUNT_LIMIT = 3
    BRANCH = "0001"

    balance = 0
    limit = 500
    statement = ""
    withdraw_count = 0
    users = []
    accounts = []

    while True:
        opcao = menu()

        if opcao == "d":
            amount = float(input("Provide the deposit amount: "))

            balance, statement = deposit(balance, amount, statement)

        elif opcao == "w":
            amount = float(input("Input the Withdraw amount: "))

            balance, statement = withdraw(
                balance=balance,
                amount=amount,
                statement=statement,
                limit=limit,
                withdraw_count=withdraw_count,
                withdraw_count_limit=WITHDRAW_COUNT_LIMIT,
            )

        elif opcao == "s":
            show_statement(balance, statement=statement)

        elif opcao == "nu":
            create_user(users)

        elif opcao == "na":
            account_number = len(accounts) + 1
            account = create_account(BRANCH, account_number, users)

            if account:
                accounts.append(account)

        elif opcao == "al":
            list_accounts(accounts)

        elif opcao == "q":
            break

        else:
            print("Invalid Choice!!!.")


main()
