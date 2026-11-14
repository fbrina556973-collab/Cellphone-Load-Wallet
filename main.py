
from load_wallet import LoadWallet


owner = input("Enter owner name: ")
number = input("Enter mobile number: ")

while True:
    try:
        balance = float(input("Enter starting balance: P"))
        if balance >= 0:
            break
        print("Starting balance cannot be negative!")
    except ValueError:
        print("Please enter a valid number!")

wallet = LoadWallet(owner, number, balance)

# Main menu
while True:
    print("\n----- MENU -----")
    print("1. Top Up Load")
    print("2. Send Load (same network)")
    print("3. Send Load (other network, with fee)")
    print("4. Show Balance")
    print("5. Exit")

    choice = input("\nChoose an option (1-5): ")

    if choice == "1":
        try:
            amount = float(input("Enter top-up amount: P"))
            wallet.top_up(amount)
        except ValueError:
            print("Invalid amount!")

    elif choice == "2":
        receiver = input("Enter receiver number: ")
        try:
            amount = float(input("Enter load amount: P"))
            wallet.send_load(receiver, amount)
        except ValueError:
            print("Invalid amount!")

    elif choice == "3":
        receiver = input("Enter receiver number: ")
        try:
            amount = float(input("Enter load amount: P"))
            wallet.send_with_fee(receiver, amount)
        except ValueError:
            print("Invalid amount!")

    elif choice == "4":
        wallet.show_balance()

    elif choice == "5":
        print("Thank you for using Cellphone Load Wallet!")
        break

    else:
        print("Invalid option! Please choose 1-5.")
