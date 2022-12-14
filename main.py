from menu import MENU, resources
print("ITEM         PRICE")
print("----         -----")
print("Espresso   - $1.50")
print("Latte      - $2.50")
print("Cappuccino - $3.00")
print(" ")
machine_on = True
while machine_on:
    choice = (input("What would you like? (Espresso/Latte/Cappuccino): ")).lower()
    if choice == "exit":
        print("Machine is powering off. Goodbye!!")
        exit()
    elif choice == "report":
        for k, v in resources.items():
            print(k, ":", v)
    elif choice == "espresso":
        if resources["water"] < MENU["espresso"]["ingredients"]["water"]:
            print("Insufficient Water..Sorry Try Again Later")
            exit()
        elif resources["coffee"] < MENU["espresso"]["ingredients"]["coffee"]:
            print("Insufficient Coffee Powder... Try Again Later")
            exit()
        else:
            print("INSERT COINS")
            print("------------")
            penny = int(input("Pennies: "))
            nickel = int(input("Nickels: "))
            dimes = int(input("Dimes: "))
            quarter = int(input("Quarters: "))
            money_inserted = ((0.25 * quarter)+(0.10 * dimes)+(0.05 * nickel)+(0.01 * penny))
            if money_inserted < MENU["espresso"]["cost"]:
                print(f"Money Inserted: ${money_inserted}")
                print(f"Required Amount: ${MENU['espresso']['cost']}")
                print("Insufficient Money. Insert coins refunded.")
            else:
                resources["money"] += 1.5
                if money_inserted > MENU['espresso']['cost']:
                    balance = money_inserted - MENU['espresso']['cost']
                    print(f"Balance Amount ${balance.__round__()} refunded.")
                resources["water"] = resources["water"] - MENU[f"{choice}"]["ingredients"]["water"]
                resources["coffee"] = resources["coffee"] - MENU[f"{choice}"]["ingredients"]["coffee"]
                print(f"Here's Your {choice}..Enjoy!!")
    elif choice == "latte":
        if resources["water"] < MENU["latte"]["ingredients"]["water"]:
            print("Insufficient Water..Sorry Try Again Later")
            exit()
        elif resources["milk"] < MENU["latte"]["ingredients"]["milk"]:
            print("Insufficient Milk... Sorry Try Again Later")
            exit()
        elif resources["coffee"] < MENU["latte"]["ingredients"]["coffee"]:
            print("Insufficient Coffee Powder... Try Again Later")
            exit()
        else:
            print("INSERT COINS")
            print("------------")
            penny = int(input("Pennies: "))
            nickel = int(input("Nickels: "))
            dimes = int(input("Dimes: "))
            quarter = int(input("Quarters: "))
            money_inserted = ((0.25 * quarter)+(0.10 * dimes)+(0.05 * nickel)+(0.01 * penny))
            if money_inserted < MENU["latte"]["cost"]:
                print(f"Money Inserted: ${money_inserted}")
                print(f"Required Amount: ${MENU['latte']['cost']}")
                print("Insufficient Money. Insert coins refunded.")
            else:
                resources["money"] += 1.5
                if money_inserted > MENU['latte']['cost']:
                    balance = money_inserted - MENU['latte']['cost']
                    print(f"Balance Amount ${balance.__round__()} refunded.")
                resources["water"] = resources["water"] - MENU[f"{choice}"]["ingredients"]["water"]
                resources["milk"] = resources["milk"] - MENU[f"{choice}"]["ingredients"]["milk"]
                resources["coffee"] = resources["coffee"] - MENU[f"{choice}"]["ingredients"]["coffee"]
                print(f"Here's Your {choice}..Enjoy!!")
    elif choice == "cappuccino":
        if resources["water"] < MENU["cappuccino"]["ingredients"]["water"]:
            print("Insufficient Water..Sorry Try Again Later")
            exit()
        elif resources["milk"] < MENU["cappuccino"]["ingredients"]["milk"]:
            print("Insufficient Milk... Sorry Try Again Later")
            exit()
        elif resources["coffee"] < MENU["cappuccino"]["ingredients"]["coffee"]:
            print("Insufficient Coffee Powder... Try Again Later")
            exit()
        else:
            print("INSERT COINS")
            print("------------")
            penny = int(input("Pennies: "))
            nickel = int(input("Nickels: "))
            dimes = int(input("Dimes: "))
            quarter = int(input("Quarters: "))
            money_inserted = ((0.25 * quarter)+(0.10 * dimes)+(0.05 * nickel)+(0.01 * penny))
            if money_inserted < MENU["cappuccino"]["cost"]:
                print(f"Money Inserted: ${money_inserted}")
                print(f"Required Amount: ${MENU['cappuccino']['cost']}")
                print("Insufficient Money. Insert coins refunded.")
            else:
                resources["money"] += 1.5
                if money_inserted > MENU['cappuccino']['cost']:
                    balance = money_inserted - MENU['cappuccino']['cost']
                    print(f"Balance Amount ${balance.__round__()} refunded.")
                resources["water"] = resources["water"] - MENU[f"{choice}"]["ingredients"]["water"]
                resources["milk"] = resources["milk"] - MENU[f"{choice}"]["ingredients"]["milk"]
                resources["coffee"] = resources["coffee"] - MENU[f"{choice}"]["ingredients"]["coffee"]
                print(f"Here's Your {choice}..Enjoy!!")