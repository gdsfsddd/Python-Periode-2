print("Hello Periode 2!")


player_name = input("Wat is je naam? ")

player_gold = 100

inventory = []

print("Welkom", player_name, "!")
print("Je begint met", player_gold, "gold.")
items = ["Sword", "Shield", "Potion", "Bow"]

for item in items:
    print(item)
gold = 100
inventory = []

while True:
    print("\n=== Fantasy Item Shop ===")
    print("1. Buy Sword (50 gold)")
    print("2. Buy Shield (40 gold)")
    print("3. Buy Potion (20 gold)")
    print("4. Buy Bow (60 gold)")
    print("5. View Inventory")
    print("6. Exit Shop")

    choice = input("\nWhat would you like to do? ")

    if choice == "1":
        if gold >= 50:
            gold -= 50
            inventory.append("Sword")
            print("You bought a Sword!")
        else:
            print("Not enough gold!")

    elif choice == "2":
        if gold >= 40:
            gold -= 40
            inventory.append("Shield")
            print("You bought a Shield!")
        else:
            print("Not enough gold!")

    elif choice == "3":
        if gold >= 20:
            gold -= 20
            inventory.append("Potion")
            print("You bought a Potion!")
        else:
            print("Not enough gold!")

    elif choice == "4":
        if gold >= 60:
            gold -= 60
            inventory.append("Bow")
            print("You bought a Bow!")
        else:
            print("Not enough gold!")

    elif choice == "5":
        print("\nYour Inventory:")
        print(inventory)
        print("Gold:", gold)

    elif choice == "6":
        print("Thanks for visiting the shop!")
        break

    else:
        print("Invalid choice. Please try again.")
match keuze:
    case 1:
        item = "Sword"
        prijs = 50

    case 2:
        item = "Shield"
        prijs = 30

    case 3:
        item = "Health Potion"
        prijs = 20

    case _:
        print("Ongeldige keuze!")

if keuze in [1, 2, 3]:
    if player_gold >= prijs:
        player_gold -= prijs
        inventory.append(item)

        print(f"Je hebt {item} gekocht!")
        print(f"Je hebt nog {player_gold} gold over.")
    else:
        print("Je hebt niet genoeg gold!")
        print(f"Je hebt nog {player_gold} gold.")
        
elif keuze == "5":
    if len(inventory) == 0:
        print("Your inventory is empty!")
    else:
        print("Your inventory:")
        for item in inventory:
            print(item)
            winkel_open = True

while winkel_open:
    keuze = input("Maak een keuze: ")

    if keuze == "6":
        print("Bedankt voor het spelen!")
        print(f"Je hebt nog {gold} gold over.")
        winkel_open = False

    elif keuze not in ["1", "2", "3", "4", "5", "6"]:
        print("Ongeldige menuoptie!")