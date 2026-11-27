def show_menu():
    print("\n=== Fantasy Item Shop ===")
    print("1. Buy Sword (50 gold)")
    print("2. Buy Shield (30 gold)")
    print("3. Buy Potion (10 gold)")
    print("4. Leave shop")
    print("5. Show inventory")
    print("6. Work (+20 gold)")
    print("7. Sell item")


def show_inventory(inventory):
    print("\n=== Inventory ===")

    if len(inventory) == 0:
        print("Your inventory is empty.")
    else:
        for item in inventory:
            print(item)


def can_buy(gold, price):
    if gold >= price:
        return True
    else:
        return False


def buy_item(gold, inventory, item_name, price):
    if can_buy(gold, price):
        gold -= price
        inventory.append(item_name)
        print(f"You bought {item_name}!")
        print(f"You have {gold} gold left.")
    else:
        print("Not enough gold!")

    return gold


def sell_item(gold, inventory):
    if len(inventory) == 0:
        print("You have no items to sell.")
        return gold

    show_inventory(inventory)

    item_name = input("Which item do you want to sell? ")

    if item_name in inventory:
        inventory.remove(item_name)
        gold += 10
        print(f"You sold {item_name} for 10 gold.")
    else:
        print("You don't have that item.")

    return gold


def work(gold):
    gold += 20
    print("You worked and earned 20 gold!")
    print(f"You now have {gold} gold.")
    return gold


def choose_difficulty():
    print("\nChoose difficulty:")
    print("1. Easy (150 gold)")
    print("2. Normal (100 gold)")
    print("3. Hard (50 gold)")

    choice = input("Choose: ")

    if choice == "1":
        return 150
    elif choice == "2":
        return 100
    elif choice == "3":
        return 50
    else:
        print("Invalid choice. Normal difficulty selected.")
        return 100


# Start of the program
inventory = []
player_gold = choose_difficulty()

running = True

while running:
    print(f"\nYou have {player_gold} gold.")
    show_menu()

    choice = input("Choose an option: ")

    match choice:
        case "1":
            player_gold = buy_item(player_gold, inventory, "Sword", 50)

        case "2":
            player_gold = buy_item(player_gold, inventory, "Shield", 30)

        case "3":
            player_gold = buy_item(player_gold, inventory, "Potion", 10)

        case "4":
            print("Thanks for visiting the shop!")
            running = False

        case "5":
            show_inventory(inventory)

        case "6":
            player_gold = work(player_gold)

        case "7":
            player_gold = sell_item(player_gold, inventory)

        case _:
            print("Invalid choice. Try again.")
